To use this, open matlab,
run 

[AllData, dataByFile] = processAllDataWithStdDev();

then you have your data in:
AllData.data or dataByFile(i).data

It takes a little bit to run.

The goal is to make something that makes sense for the checkHeatExchangers
file to use as a cut-off fouling factor calculation value

(I'm checking whether each heat exchanger will work by estimating the fouling
factor necessary to acheive the heat transfer in the 
problem statement's specified system. If it
is above my estimated value, the heat exchanger will work. Otherwise, it
should
not. Negative values of the fouling factor mean that there is no
way to get the required heat transfer from the heat exchanger in question.)
