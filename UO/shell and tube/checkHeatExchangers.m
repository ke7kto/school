function [lowPressureExchangers, highPressureExchangers, foulingCalculated] = checkHeatExchangers()
    filename = char('hxoptions.xlsx');
    [hxFile,hxFileText]  = xlsread(filename,'Sheet1','A2:G800');
    modelNumbers = hxFileText(:,1);
    nTubes = hxFile(:,1);
    surfaceArea = hxFile(:,2);
    innerD = hxFile(:,3);
    outerD = hxFile(:,4);
    baffleSpacing = hxFile(:,5);
    lTube = hxFile(:,6); 
    steelKs = [13.4, 15.2, 18.3,21.3];
    steelKTs = [300, 400, 600,800];
    steelKTs=steelKTs-273.15;

    function kSteel = kSteelT(temp)
        if temp > 0;
            kSteel = interp1(steelKTs,steelKs,temp,'linear');
        else
            kSteel = interp1(steelKTs,steelKs,200);
        end
    end
    surfaceArea = surfaceArea .* 0.092903;
    innerD = innerD .* 0.0254 ;
    outerD = outerD .* 0.0254 ;
    lTube = lTube .* 0.0254 ;
    baffleSpacing=baffleSpacing .* 0.0254;
    innerArea = innerD.*pi.*lTube.*nTubes;
    outerArea = outerD.*pi.*lTube.*nTubes;
    g = 9.80;
    if ~exist('ResultsByFile');
    [ResultsByFile, ResultsList] = processAllDataWithStdDev();
    end
    data=ResultsByFile(26).data;
    
    
    specPointFlow = 200;                    %gpm
    specPointFlow = specPointFlow .* 0.0000631; %m^3/s
    specPointV = specPointFlow./(pi*innerD.^2./4)./nTubes;
    specPointPressure1 = 100;               %psig steam
    specPointPressure2 = 300;               %psig steam
    ambientPressure = mean(ResultsList.ambientPressure);
    steamPressure1 = specPointPressure1.*101325/14.696 + ambientPressure;
    steamPressure2 = specPointPressure2.*101325/14.696 + ambientPressure;
    
    TwaterIn = 25;
    TwaterOut = 75;
    outletWaterT = TwaterOut;
    inletWaterT = TwaterIn;
    hWaterHeated = arrayfun(@GetEnthalpyTP,outletWaterT,ambientPressure)-arrayfun(@GetEnthalpyTP,inletWaterT,ambientPressure);
    averageWaterT = (inletWaterT+outletWaterT)./2;
    densityWater = GetDensity(averageWaterT,ambientPressure);
    mFlowWater = specPointFlow.*densityWater;
    %steam properties
    steamTemp1 = GetSteamTemp(steamPressure1);
    densityLiqSteam1 = arrayfun(@GetLDensity,steamPressure1);
    densityVapSteam1 = arrayfun(@GetVDensity,steamPressure1);
    hVaporization1 = arrayfun(@GetHeatVap,steamPressure1);
    mFlowSteam1 = hWaterHeated.*mFlowWater./hVaporization1;
    kLiqSteam1 = arrayfun(@GetLiqThermalCond,steamPressure1);
    viscLiqSteam1 = arrayfun(@GetViscLiqSteam,steamPressure1);
    cpLiqSteam1 = arrayfun(@GetLHeatCapacity,steamPressure1);
    
    steamTemp2 = GetSteamTemp(steamPressure2);
    densityLiqSteam2 = arrayfun(@GetLDensity,steamPressure2);
    densityVapSteam2 = arrayfun(@GetVDensity,steamPressure2);
    hVaporization2 = arrayfun(@GetHeatVap,steamPressure2);
    mFlowSteam2 = hWaterHeated.*mFlowWater./hVaporization2;
    kLiqSteam2 = arrayfun(@GetLiqThermalCond,steamPressure2);
    viscLiqSteam2 = arrayfun(@GetViscLiqSteam,steamPressure2);
    cpLiqSteam2 = arrayfun(@GetLHeatCapacity,steamPressure2);
    
    
    lmtd1 = ((steamTemp1 - outletWaterT) - (steamTemp1 - inletWaterT))./(log((steamTemp1 - outletWaterT)./(steamTemp1 - inletWaterT)));
    lmtd2 = ((steamTemp2 - outletWaterT) - (steamTemp2 - inletWaterT))./(log((steamTemp2 - outletWaterT)./(steamTemp2 - inletWaterT)));
    
    %Fluid characteristics
    viscWater = GetViscosity(averageWaterT,ambientPressure);
    cpWater = GetLHeatCapacity(ambientPressure);
    vPipe = specPointFlow./(pi.*innerD.^2./4)./nTubes;
    ReWater = densityWater.*vPipe .*innerD./viscWater;
    kWater = arrayfun(@GetThermalCond,averageWaterT,ambientPressure);
    PrandtlWater = cpWater.*viscWater./kWater;
    NusseldtWater = 0.023.*ReWater.^(4./5).*PrandtlWater.^(.4);
    hInner = NusseldtWater./innerD.*kWater;
    %Fouling characteristics
    %[P1,S1] = polyfit(ResultsList.pipeV,ResultsList.Rfoul,1);
    %[P1_1,S1_1]=polyfit(ResultsList.pipeV,ResultsList.Rfoul,1);
    calculatedFoulingFactor1 = mean(ResultsList.Rfoul);
    err1 = 2.*std(ResultsList.Rfoul);
    calculatedFoulingFactor2 = calculatedFoulingFactor1+err1;
    calculatedFoulingFactor1 = calculatedFoulingFactor2;
    %calculatedFoulingFactor2 = polyval(P1_1,vPipe);
    %calculatedFoulingFactor1 = 7.3885e-5;
    %calculatedFoulingFactor2 = calculatedFoulingFactor1;
%     F = scatteredInterpolant(data.massFlowWater,data.steamPressure,data.Rfoul);
%     x = linspace(min(data.massFlowWater),mFlowWater);
%     y = linspace(min(data.steamPressure),steamPressure2);
%     calculatedFoulingFactor1 = F(mFlowWater,steamPressure1);
%     calculatedFoulingFactor2 = F(mFlowWater,steamPressure2);
%     calculatedFoulingFactor2 = mean(data.Rfoul);
%     calculatedFoulingFactor1 = mean(data.Rfoul);
    %surface properties/ convection coefficients
    Tsurface2 = steamTemp1 -5;
    Tsurface = steamTemp1 - lmtd1;
    iterations = 0;
    boolean = 0;
    hWaterHeated = (GetEnthalpyTP(TwaterOut,ambientPressure) - GetEnthalpyTP(TwaterIn,ambientPressure));
    q = hWaterHeated*mFlowWater;
    UA1 = q./lmtd1;
    UA2 = q./lmtd2;
    while (~((isequal(Tsurface2, Tsurface)|| boolean)))
        Tsurface = Tsurface2;
        %initial guess at a Nusseldt number
        
        
        hVapPrime1 = hVaporization1 + 0.68.*cpLiqSteam1.*(steamTemp1 - Tsurface);
        NusseldtSteam = 0.943.*(densityLiqSteam1.*g.*(densityLiqSteam1 - densityVapSteam1).*hVapPrime1.*baffleSpacing.^3./...
            (viscLiqSteam1.*kLiqSteam1.*(steamTemp1 - Tsurface))).^(1/4);
        hOuter = 0.943.*(g.*densityLiqSteam1.*(densityLiqSteam1-densityVapSteam1).*kLiqSteam1.^3.*hVapPrime1./...
            (viscLiqSteam1.*(steamTemp1-Tsurface).*baffleSpacing)).^(1/4);
        condRes = log(outerD./innerD)./(2*pi.*nTubes.*kSteelT((Tsurface+averageWaterT)./2));
        
        Rfoul = innerArea./UA1 - innerArea./(hOuter.*outerArea) - innerArea.*condRes - 1./hInner;
        Tsurface2 = steamTemp1-q.*(1./(hOuter.*outerArea));
        iterations=iterations+1;
        if or(iterations > 10000,Tsurface2 < 0)
            if max(Tsurface2-Tsurface)<1e-3
                Tsurface2= Tsurface;
                Tsurface = Tsurface2;
                boolean = 1;
            else
                Tsurface2=Tsurface;
                boolean = 1;
                fprintf('%f',max(Tsurface2-Tsurface));
            end
        end
    end
    lowPressureExchangers = [];
    for i=1:numel(nTubes);
        lowPressureExchangers = [lowPressureExchangers, struct('HXNames',modelNumbers(i),'HXFouling',Rfoul(i),'willWork',(Rfoul(i) - calculatedFoulingFactor1)>0)];
    end
    Tsurface2 = steamTemp2 -5;
    Tsurface = steamTemp2 - lmtd2;
    while (~((isequal(Tsurface2, Tsurface)|| boolean)))
        Tsurface = Tsurface2;
        %initial guess at a Nusseldt number
        
        
        hVapPrime2 = hVaporization2 + 0.68.*cpLiqSteam2.*(steamTemp2 - Tsurface);
        NusseldtSteam = 0.943.*(densityLiqSteam2.*g.*(densityLiqSteam2 - densityVapSteam2).*hVapPrime2.*baffleSpacing.^3./...
            (viscLiqSteam2.*kLiqSteam2.*(steamTemp2 - Tsurface))).^(1/4);
        hOuter = 0.943.*(g.*densityLiqSteam2.*(densityLiqSteam2-densityVapSteam2).*kLiqSteam2.^3.*hVapPrime2./...
            (viscLiqSteam2.*(steamTemp2-Tsurface).*baffleSpacing)).^(1/4);
        condRes = log(outerD./innerD)./(2*pi.*nTubes.*kSteelT((Tsurface+averageWaterT)./2));
        
        Rfoul = innerArea./UA2 - innerArea./(hOuter.*outerArea) - innerArea.*condRes - 1./hInner;
        Tsurface2 = steamTemp2-q.*(1./(hOuter.*outerArea));
        iterations=iterations+1;
        if Tsurface2 < (steamTemp2 - lmtd2);
            Tsurface2 = steamTemp2 - lmtd2;
        end
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
    highPressureExchangers = [];
    for i=1:numel(nTubes);
        highPressureExchangers = [highPressureExchangers, struct('HXNames',modelNumbers(i),'foulingForHX',Rfoul(i),'willWork',(Rfoul(i) - calculatedFoulingFactor2)>0)];
    end
    foulingCalculated = [calculatedFoulingFactor1, calculatedFoulingFactor2];
    fprintf('Models that should work under low pressure steam\n\n');
    for i=1:numel(lowPressureExchangers)
        if lowPressureExchangers(i).willWork
            fprintf('%s\n',lowPressureExchangers(i).HXNames);
        end
    end
    fprintf('\nModels that should work under high pressure steam\n\n');
    for i=1:numel(highPressureExchangers)
        if highPressureExchangers(i).willWork
            fprintf('%s\n',highPressureExchangers(i).HXNames);
        end
    end
    
    
    
    
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
