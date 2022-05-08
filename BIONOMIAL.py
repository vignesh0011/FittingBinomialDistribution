import numpy as np
import math
import scipy.stats

X=[0,1,2,3,4,5,6]
f=[13,25,52,68,32,16,4]
n=6
N=np.sum(f)
mean=np.inner(X,f)/N
p=mean/n
q=1-p
Pr=list(); E=list(); xi=list()
print("  X P(X=x) Obs.Fr  Ex.Fre   xi ")
print("----------------------------------")
for x in range(7):
    c=math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
    Pr.append(c*p*x*q*(n-x))
    E.append(Pr[x]*N)
    xi.append((f[x]-E[x])**2/E[x])
    print("%2.2f %2.2f  %4.2f   %3.2f  %3.2f"%(x,Pr[x],f[x],E[x],xi[x]))
print("----------------------------------")
cal_chi2=np.sum(xi)
print("Calculated value of Chi square is %4.2f"%cal_chi2)
tab_chi2=scipy.stats.chi2.ppf(1-.01, df=n)
print("Table value of Chi square at 1  level is %4.2f"%tab_chi2)
if cal_chi2<tab_chi2:
    print("The given data can be fitted in binomial distribution at 1% LOS")
else:
    print("The given data cannot be fitted in binomial distribution at 1% LOS")
