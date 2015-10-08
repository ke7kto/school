function [AllDataByFile AllData] = processAllDataWithStdDev()
    list = dir('data_*');
    i=0;
    time=0;
    mFlowWater=0;
    mFlowSteam=0;
    Rfoul=0;
    steamPressure=0;
    AllDataByFile = [];
    averageFlowWater = [];
    averageFlowSteam = [];
    averageRfoul = [];
    averageSteamPressure = [];
    AllData = struct('Time',[],'massFlowWater',[],'massFlowSteam',[],'Rfoul',[],'steamPressure',[],'ambientPressure',[],'pipeV',[]);
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
        AllData.ambientPressure = [AllData.ambientPressure;allData.ambientPressure(goodPoints)];
        AllData.pipeV = [AllData.pipeV;allData.pipeV(goodPoints)];
    end
    for dataFile = AllDataByFile;
       averageFlowWater = [averageFlowWater; mean(dataFile.data.massFlowWater)];
       averageFlowSteam = [averageFlowSteam; mean(dataFile.data.massFlowSteam)];
       averageRfoul = [averageRfoul; mean(dataFile.data.Rfoul)];
       averageSteamPressure = [averageSteamPressure; mean(dataFile.data.steamPressure)];
        
    end
    AllDataByFile = [AllDataByFile struct('name','Averages','data',struct('Rfoul',averageRfoul,'massFlowWater',averageFlowWater,'massFlowSteam',averageFlowSteam,'steamPressure',averageSteamPressure))];
end
