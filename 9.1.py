import pandas as pd
mathd = {'Student': ['Ice Bear','Panda','Grizzly'], 'Math': [80,95,79]}
math = pd.DataFrame(mathd, columns=['Student','Math'])
elecd = {'Student': ['Ice Bear','Panda','Grizzly'], 'Electronics': [85,81,83]}
elec = pd.DataFrame(elecd, columns=['Student','Electronics'])
geasd = {'Student': ['Ice Bear','Panda','Grizzly'], 'GEAS': [90,79,93]}
geas = pd.DataFrame(geasd, columns=['Student','GEAS'])
esatd = {'Student': ['Ice Bear','Panda','Grizzly'], 'ESAT': [93,89,88]}
esat = pd.DataFrame(esatd, columns=['Student','ESAT'])
A = pd.merge(math,elec, how = 'right', on = 'Student')
B = pd.merge(A, geas, how = 'right', on = 'Student')
C = pd.merge(B, esat, how = 'right', on = 'Student')