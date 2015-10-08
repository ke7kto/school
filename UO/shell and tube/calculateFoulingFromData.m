[L1 L2]=processAllDataWithStdDev();
Rfoul=L1(26).data.Rfoul; 
mFlowWater = L1(26).data.mFlowWater;
Reference to non-existent field 'mFlowWater'.
 
mFlowWater = L1(26).data.massFlowWater;
steamPressure = L1(26).data.steamPressure;
F = scatteredInterpolant(massFlowWater,steamPressure,Rfoul,'linear');
 
F = scatteredInterpolant(mFlowWater,steamPressure,Rfoul,'linear');
point1x = 12.4961;
point1y = mean(L2.ambientPressure)+100*101325/14.696;
point2y = mean(L2.ambientPressure)+300*101325/14.696;
 
[P1,S1] = polyfit(mFlowWater,Rfoul,1);
[P2,S2] = polyfit(steamPressure,Rfoul,1);
x = linspace(0,point1x);
xConst = ones(numel(x)).*point1x;
y1Const = ones(numel(x)).*point1y;
y2Const = ones(numel(x)).*point2y;
y = linspace(0,point1y);
plot3(mFlowWater,steamPressure,Rfoul,'bo');
hold on;
xlabel('flow');ylabel('pressure');zlabel('foul');
plot3(x,y1Const,polyval(P1,x),'g--');
plot3(xConst,y,polyval(P2,y),'r--');
uncertainty=polyval(P1,point1x)-polyval(P2,point1y);
fouling1 = polyval(P1,point1x);
fouling2 = polyval(P1,point1x);
