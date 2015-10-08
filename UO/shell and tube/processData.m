function Answer = processData(filename)
%If this were a csv instead ->%dataFile = importdata(filename);
filename = char(filename);
dataFile = xlsread(filename);
time = dataFile(:,1);                  %sec
waterLevel = dataFile(:,2);            %ft
flowRate = dataFile(:,3);              %gpm
houseSteamPressure = dataFile(:,4);    %psig
steamPressure = dataFile(:,5);         %psig
inletWaterT = dataFile(:,6);           %C
outletWaterT = dataFile(:,7);          %C
waterFeedT = dataFile(:,8);            %C
ambientT = dataFile(:,9);              %C
ambientP = dataFile(:,10);             %kPa
flowSP = dataFile(:,11);               %gpm
flowControlOP = dataFile(:,12);        %percent open
levelSP = dataFile(:,13);              %ft
levelControlOP = dataFile(:,14);        %Percent
steamSP = dataFile(:,15);               %Percent
steamControlOP = dataFile(:,16);        %Percent

baffleSpacing = 4;                       %m
outerD = 0.00635;                       %m
outerPerimeter = pi.*outerD;            %m
hxArea = 7.3 * 0.092903;                %m^2
wallThick = .000559;                     %m
innerD = outerD-2.*wallThick;
nTubes = 56;                            %Tubes
g = 9.80;                               %m/s^2
steelKs = [13.4, 15.2];
steelKTs = [300-273.15, 400-273.15];

    function kSteel = kSteelT(temp)
        kSteel = interp1(steelKTs,steelKs,temp,'linear');
    end
%Now we convert to SI
ambientP = ambientP.*1000;              %Pa
steamPressure = steamPressure .* 6894.75729 + ambientP; %Pa
flowRate = flowRate .*6.30901964e-5;    %m^3/s
lTube = 24*0.0254;                      %m
baffleSpacing = baffleSpacing.*0.0254;
lTube2 = baffleSpacing;

%Now for derived units
innerArea = innerD.*pi.*lTube.*nTubes;  %m^2
outerArea = outerD.*pi.*lTube.*nTubes;  %m^2

steamTemp = arrayfun(@GetSteamTemp,steamPressure);
lmtd = ((steamTemp - outletWaterT) - (steamTemp - inletWaterT))./(log((steamTemp - outletWaterT)./(steamTemp - inletWaterT))); 
hVaporization = arrayfun(@GetHeatVap,steamPressure);
hWaterHeated = arrayfun(@GetEnthalpyTP,outletWaterT,ambientP)-arrayfun(@GetEnthalpyTP,inletWaterT,ambientP);
vPipe = flowRate ./(pi*innerD.^2./4)./nTubes;
averageWaterT = (inletWaterT + outletWaterT)./2;
densityWater = arrayfun(@GetDensity,averageWaterT,ambientP);
viscWater = arrayfun(@GetViscosity,averageWaterT,ambientP);
cpWater = arrayfun(@GetHeatCapacity,averageWaterT,ambientP);
densityLiqSteam = arrayfun(@GetLDensity,steamPressure);
densityVapSteam = arrayfun(@GetVDensity,steamPressure);
mFlowWater = flowRate .* densityWater;
mFlowSteam = hWaterHeated.*mFlowWater./hVaporization;                       %kg/s
kWater = arrayfun(@GetThermalCond,averageWaterT,ambientP);
kLiqSteam = arrayfun(@GetLiqThermalCond,steamPressure);
viscLiqSteam = arrayfun(@GetViscLiqSteam,steamPressure);
cpLiqSteam = arrayfun(@GetLHeatCapacity,steamPressure);
%Solution starts (more or less) here
%tauSteam = mFlowSteam./outerPerimeter./nTubes./(lTube./baffleSpacing);
%ReSteam = 4.*tauSteam./viscLiqSteam;
ReWater = densityWater.*vPipe .*innerD./viscWater;
PrandtlWater = cpWater.*viscWater./kWater;
NusseldtWater = 0.023.*ReWater.^(4./5).*PrandtlWater.^(.4);
hInner = NusseldtWater./innerD.*kWater;

UA = mFlowWater.*hWaterHeated./lmtd;                                             
q = mFlowWater.*hWaterHeated;
%This is where it gets fun! Making a guess T surface to solve with
Tsurface = steamTemp - 5;
Tsurface2 = steamTemp - lmtd;
iterations=0;
boolean = 0;
while (~((isequal(Tsurface2, Tsurface)|| boolean)))
    Tsurface = Tsurface2;
    %initial guess at a Nusseldt number
    
    
    hVapPrime = hVaporization + 0.68.*cpLiqSteam.*(steamTemp - Tsurface);
    NusseldtSteam = 0.943.*(densityLiqSteam.*g.*(densityLiqSteam - densityVapSteam).*hVapPrime.*baffleSpacing.^3./...
        (viscLiqSteam.*kLiqSteam.*(steamTemp - Tsurface))).^(1/4);
    hOuter = 0.943.*(g.*densityLiqSteam.*(densityLiqSteam-densityVapSteam).*kLiqSteam.^3.*hVapPrime./...
        (viscLiqSteam.*(steamTemp-Tsurface).*baffleSpacing)).^(1/4);
    condRes = log(outerD./innerD)./(2*pi.*nTubes.*kSteelT((Tsurface+averageWaterT)./2));
    
    Rfoul = innerArea./UA - innerArea./(hOuter.*outerArea) - innerArea.*condRes - 1./hInner;
    Tsurface2 = steamTemp-q.*(1./(hOuter.*outerArea));
    iterations=iterations+1;
    if iterations > 10000
        if max(Tsurface2-Tsurface)<1e-3
            Tsurface2= Tsurface;
            Tsurface = Tsurface2;
            boolean = 1;
        else
            fprintf('%f',max(Tsurface2-Tsurface));
        end
    end
end
Answer = struct('Time',time,'massFlowWater',mFlowWater,'massFlowSteam',mFlowSteam,'Rfoul',Rfoul,'steamPressure',steamPressure,'ambientPressure',ambientP,'pipeV',vPipe);
end
%Input C, Pascals
%Output W/m K
function k= GetThermalCond(temperature,pressure) 
    k = XSteam('tc_pT',pressure/1e5,temperature);
end
%Input C, Pascals
%Output W/m K
function k= GetLiqThermalCond(pressure)
    k = XSteam('tcL_p',pressure/1e5);
end
%Input Pascals
%Output kg/m^3
function rho = GetVDensity(pressure)
    rho = XSteam('rhoV_p',pressure/1e5);
end
%Input Pascals
%Output kg/m^3
function rho = GetLDensity(pressure)
    rho = XSteam('rhoL_p',pressure/1e5);
end
%Input Pascals
%Output kg/m^3
function rho = GetDensity(temperature,pressure)
    rho = XSteam('rho_pT',pressure/1e5,temperature);
end
%Input C, Pa
%output J/kg
function H = GetEnthalpyTP(temperature,pressure)
    H = XSteam('h_pT',pressure/1e5,temperature)*1e3;
end
%Input Pa
%output J/kg
function H = GetHeatVap(pressure_Pa)
    H = (XSteam('hV_p',pressure_Pa/1e5)-XSteam('hL_p',pressure_Pa/1e5))*1e3; 
end
%Input Pa
%Output C
function Temp= GetSteamTemp(pressure_Pa)
    Temp = XSteam('Tsat_p',pressure_Pa/1e5);
end
%Input Pa
%Output J/kg*K
function cp = GetLHeatCapacity(pressure)
    cp = XSteam('CpL_p',pressure/1e5)*1e3;
end
%Input C, Pa
%Output J/kg*K
function cp = GetHeatCapacity(temperature,pressure)
    cp = XSteam('Cp_pT',pressure/1e5,temperature)*1e3;
end
%Input Pa
%Output N*s/m^2
function visc = GetViscLiqSteam(pressure)
    h = XSteam('hL_p',pressure/1e5);
    visc = XSteam('my_ph',pressure/1e5,h);
end
%Input C, Pa
%Output N*s/m^2
function visc = GetViscosity(temperature,pressure)
    visc = XSteam('my_pT',pressure/1e5,temperature);
end
