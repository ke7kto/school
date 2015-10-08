if(~exist('L1'))
    [L1, L2]=processAllDataWithStdDev();
end
massFlowSettings = [25,30,35,38,40,45,50].*6.3090199467e-5.*998;
steamPressureSettings = [15,20,25,35,45].*101325./14.696+mean(L2.ambientPressure);
j=0;
steamRates = zeros(numel(steamPressureSettings),1);
RfoulSteam = zeros(numel(massFlowSettings),1);
massRates =  zeros(numel(steamPressureSettings),1);
RfoulWater = zeros(numel(steamPressureSettings),1);
steamInd = zeros(numel(massFlowSettings));
flowInd = zeros(numel(steamPressureSettings));
for i=1:numel(L2.massFlowWater);
    [minimum,index]=min(abs(massFlowSettings-L2.massFlowWater(i)));
    steamInd(index)=steamInd(index)+1;
    steamRates(index,steamInd(index))= L2.steamPressure(i);
    RfoulSteam(index,steamInd(index))=L2.Rfoul(i);
    
end
for j=1:numel(L2.steamPressure)
   [~,index2]=min(abs(steamPressureSettings-L2.steamPressure(j))); 
   flowInd(index2)=flowInd(index2)+1;
   massRates(index2,flowInd(index2))= L2.massFlowWater(j);
   RfoulWater(index2,flowInd(index2))= L2.Rfoul(j); 
    
end

    
close all;
set(groot,'defaultAxesColorOrder',[1 0 0;0 1 0;0 0 1],...
      'defaultAxesLineStyleOrder','-|--|:');
color = [1 0 0;0 1 0;0 0 1;.5 .5 0;0 .5 .5;.5 0 .5;.3 .3 .3;0 1 0;0 0 1;.5 .5 0;0 .5 .5;.5 0 .5];
ls = ['-','--','-.','-','--','-.','-','--'];
ps = ['o','+','v','*','.','x','p','h'];
mFlowString = [sprintf('%d [gpm]',25)];
mFlowString = [mFlowString; sprintf('%d [gpm]',30)];
mFlowString = [mFlowString; sprintf('%d [gpm]',35)];
mFlowString = [mFlowString; sprintf('%d [gpm]',38)];
mFlowString = [mFlowString; sprintf('%d [gpm]',40)];
mFlowString = [mFlowString; sprintf('%d [gpm]',45)];
mFlowString = [mFlowString; sprintf('%d [gpm]',50)];
hold on;
for j=1:numel(massFlowSettings);
    notZeros = steamRates(j,:)>0;
    %plot(steamRates(j,notZeros),RfoulSteam(j,notZeros),colors(j));
    [p,S] = polyfit(steamRates(j,notZeros),RfoulSteam(j,notZeros),1);
    x = linspace(min(steamRates(j,notZeros))-0.5e5,max(steamRates(j,notZeros))+.5e5,6);
    [y,E]=polyval(p,x,S);
    F = scatteredInterpolant([steamRates(j,notZeros);RfoulSteam(j,notZeros)]',RfoulSteam(j,notZeros)');
    y1 = F([steamRates(j,notZeros);RfoulSteam(j,notZeros)]');
%     h(j)=plot(steamRates(j,notZeros),y1-2.*E);
%     set(h(j),'Color',[1,0,0]);
%     set(h(j),'LineStyle',ls(j));
    h2(j)=errorbar(x,y,2.*E);
    hc = get(h2(j),'Children');
    set(hc(1),'Color',color(j,:));
    set(hc(1),'LineStyle', ls(j));
    set(hc(2),'Color',[0,0,0]);
    h3(j)=plot(steamRates(j,notZeros),y1);
    set(h3(j),'LineStyle','none');
    set(h3(j),'Marker',ps(j));
    set(h3(j),'Color',color(j,:));
    set(h3(j),'DisplayName',mFlowString(j,:));
    
%    set(h2(j),'DisplayName',mFlowString(j,:));
%     h3(j)=plot(steamRates(j,notZeros),y1+2.*E);
%     set(h3(j),'Color', [0,0,1]);
%     set(h3(j),'LineStyle', ls(j));
end
legend(h3);
xlabel('Steam Pressure (Pa)');
ylabel('R_{foul}');
title('Fouling Factor as a function of steam pressure');
fig1 = findobj('Type','figure');
saveas(fig1,'SteamPressureVsFouling.png');
close all;


color = [1 0 0;0 1 0;0 0 1;.5 .5 0;0 .5 .5;.5 0 .5;.3 .3 .3;0 1 0;0 0 1;.5 .5 0;0 .5 .5;.5 0 .5];
ls = ['-','--','-.','-','--','-.','-','--'];
ps = ['o','+','v','*','.','x','p','h'];
mFlowString =              [sprintf('%d [psi]',15)];
mFlowString = [mFlowString; sprintf('%d [psi]',20)];
mFlowString = [mFlowString; sprintf('%d [psi]',25)];
mFlowString = [mFlowString; sprintf('%d [psi]',35)];
mFlowString = [mFlowString; sprintf('%d [psi]',45)];
hold on;
maxResistance = 0;
specPointFlow = 200;                    %gpm
specPointFlow = specPointFlow .* 0.0000631; %m^3/s
for j=1:numel(steamPressureSettings);
    if j ~= 2
    notZeros = massRates(j,:)>0;
    %plot(steamRates(j,notZeros),RfoulSteam(j,notZeros),colors(j));
    [p,S] = polyfit(massRates(j,notZeros),RfoulWater(j,notZeros),1);
    x = linspace(min(massRates(j,notZeros))-0.5,max(massRates(j,notZeros))+.5,6);
    [y,E]=polyval(p,x,S);
    F = scatteredInterpolant([massRates(j,notZeros);RfoulWater(j,notZeros)]',RfoulWater(j,notZeros)');
    y1 = F([massRates(j,notZeros);RfoulWater(j,notZeros)]');
%     h(j)=plot(steamRates(j,notZeros),y1-2.*E);
%     set(h(j),'Color',[1,0,0]);
%     set(h(j),'LineStyle',ls(j));
    [maxResistanceTest,maxResErr] = polyval(p, specPointFlow,S);
    if maxResistanceTest+maxResErr.*2 > maxResistance;
        maxResistance = maxResistanceTest+maxResErr.*2;
    end
    h2(j)=errorbar(x,y,2.*E);
    hc = get(h2(j),'Children');
    set(hc(1),'Color',color(j,:));
    set(hc(1),'LineStyle', ls(j));
    set(hc(2),'Color',[0,0,0]);
    h3(j)=plot(massRates(j,notZeros),y1);
    set(h3(j),'LineStyle','none');
    set(h3(j),'Marker',ps(j));
    set(h3(j),'Color',color(j,:));
    set(h3(j),'DisplayName',mFlowString(j,:));
    end
%    set(h2(j),'DisplayName',mFlowString(j,:));
%     h3(j)=plot(steamRates(j,notZeros),y1+2.*E);
%     set(h3(j),'Color', [0,0,1]);
%     set(h3(j),'LineStyle', ls(j));
end
h3 = [h3(1),h3(3:numel(steamPressureSettings))];
legend(h3);
xlabel('Flow Rate (m^3/s)');
ylabel('R_{foul}');
title('Fouling Factor as a function of flow rate');
fig1 = findobj('Type','figure');
saveas(fig1,'FlowVsFouling.png');

%legend(h2(1:7));

