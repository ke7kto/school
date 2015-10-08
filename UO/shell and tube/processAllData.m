function [AllDataByFile AllData] = processAllData()
    list = dir('data_*');
    i=0;
    time=0;
    mFlowWater=0;
    mFlowSteam=0;
    Rfoul=0;
    steamPressure=0;
    AllDataByFile = [];
    AllData = struct('Time',[],'massFlowWater',[],'massFlowSteam',[],'Rfoul',[],'steamPressure',[]);
    for listNames = {list.name};
        i=i+1;
        allData = processData(listNames);
        goodPoints = and(and(isfinite(allData.Rfoul),isfinite(allData.massFlowWater)),and(isfinite(allData.massFlowSteam),isfinite(allData.steamPressure)));
        AllDataByFile = [AllDataByFile struct('name',listNames,'data',allData)];
        AllData.Time = [AllData.Time; allData.Time(goodPoints)];
        AllData.massFlowWater = [AllData.massFlowWater; allData.massFlowWater(goodPoints)];
        AllData.massFlowSteam = [AllData.massFlowSteam; allData.massFlowSteam(goodPoints)];
        AllData.Rfoul         = [AllData.Rfoul; allData.Rfoul(goodPoints)];
        AllData.steamPressure = [AllData.steamPressure; allData.steamPressure(goodPoints)];
    end
end
function getItDone()
[ResultsByFile ResultsList] = processAllData();

end