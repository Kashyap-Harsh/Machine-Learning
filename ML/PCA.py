import numpy as np
import statistics
x1 = [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1]
x2 = [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]
n= len(x1)
x1m = statistics.mean(x1)
x2m = statistics.mean(x2)
x1d=[]
x2d=[]
for i in range(n):
    x1d.append(x1[i]-x1m)
    x2d.append(x2[i]-x2m)
covx1x1=0
covx1x2=0
covx2x1=0
covx2x2=0
for i in range(n):
    covx1x1=covx1x1+x1[i]*x1[i]
    covx1x2=covx1x2+x1[i]*x2[i]
    covx2x1=covx2x1+x2[i]*x1[i]
    covx2x2=covx2x2+x2[i]*x2[i]
covx1x1=covx1x1/(n-1)
covx1x2=covx1x2/(n-1)
covx2x1=covx2x1/(n-1)
covx2x1=covx2x1/(n-1)
A = np.array([[covx1x1, covx1x2],[covx2x1, covx2x2]])
e1, e2= np.linalg.eig(A)



