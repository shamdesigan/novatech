import pandas as pd

 

dataMatrix = {"D1":[135, 137, 136, 138, 138],

              "D2":[43,   42, 42, 42, 42],

              "D3":[72, 73, 72, 72, 73],

              "D4":[100, 102, 100, 103, 104]

             };

       

dataFrame = pd.DataFrame(data=dataMatrix);

 

print("DataFrame:");

print(dataFrame);

 

print("Mean:Computed column-wise:");

meanData = dataFrame.mean();

print(meanData);

 

print("Mean:Computed row-wise:");

meanData = dataFrame.mean(axis=1);

print(meanData);

 

print("Median:Computed column-wise:");

medianData = dataFrame.median();

print(medianData);

 

print("Median:Computed row-wise:");

medianData = dataFrame.median(axis=1);

print(medianData);

 

print("Mode:Computed column-wise:");

modeData = dataFrame.mode();

print(modeData);

 

print("Mode:Computed row-wise:");

modeData = dataFrame.mode(axis=1);

print(modeData);