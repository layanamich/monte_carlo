

'''
1. Generate a uniform distribution on (0, 1)
2. Transform to a Gaussian Distribution
3. Plot Histogram of Gaussian Distribution
4. Fit Gaussian to Histogram
5. Report Parameters: μ, σ, χ
'''
import numpy as np
import LT.box as B
# Random Number Generator
from scipy import random
# Parameter Module
import LT_Fit.parameters as P
# Genfit module.
import LT_Fit.gen_fit as G
import matplotlib.pyplot as plt
import math


# Data Points
N = 4000. 
# Bins for the Histogram
bins = 40 
 # Histogram Limits
x_min = -4
x_max =4
#1. Generate a uniform distribution on (0, 1)
randNum = np.zeros(int(N))
for i in range(int(N)):
    randNum[i] = random.uniform(0.,1.)

#2. Transform to a Gaussian Distribution
# Transformation Method
def UniformToGauss(u1, u2):
    ''' If u1 and u2 are uniform on (0,1), then z1 and z2
    are independent and Gaussian distributed with μ=0., σ=1.
    '''
    v1 = np.sin(2.*np.pi*u1)*np.sqrt(-2.*np.log(u2))
    v2 = np.cos(2.*np.pi*u1)*np.sqrt(-2.*np.log(u2))
    return v1, v2

i = 0
while i < int(N):
    randNum[i], randNum[i+1] = UniformToGauss(randNum[i], randNum[i+1])
    i += 2

'''# Naive Method Using in-built Random Dist. Function
for i in range(int(N)):
randNum[i] = np.random.randn() # From Gaussian Dist. with μ=0, σ=1
#'''
#3. Plot Histogram of Gaussian Distribution
title = "Gaussian Distribution\ n \
    from the Transformation of a Uniform Random Distribution"
h = B.histo(randNum, range=(x_min,x_max), bins=bins, title = title,
xlabel = 'x-value', ylabel = 'Frequency')
hx = h.bin_center
hy = h.bin_content
dy = np.sqrt(hy)
#4. Gaussian Function Fitting to Histogram
mu = P.Parameter(0.0003, 'muG')
sig = P.Parameter(1.0001, 'sigG')
norm = P.Parameter(803.0, 'normG')

def Gaussian(x):
        value = norm()*(1./sig())*(1./np.sqrt(2.*np.pi)) \
            *np.exp(-0.5*((x-mu())/sig())**2)
        return value
line = G.genfit(Gaussian, [mu, sig, norm], x = hx, y = hy)


#B.plot_line(line.xpl, line.ypl, color = 'red')
fig, ax = plt.subplots()
ax.plot(line.xpl,line.ypl, linestyle='solid', c='red', lw=1.5,
alpha=0.8, label='Best Fit Gaussian')
ax.legend(loc='best', frameon=False)
ax.text(1.27, 300, r'$g(x) = \frac{N_c}{\sigma\sqrt{2\cdot\pi}}exp[\frac{-1}{2}(\frac{x-\mu}{\sigma})^2]$'
        ,fontsize=9)
ax.text(3.,275, r'$\mu =${:.2f}'.format(mu.value),fontsize=8)
ax.text(3.,265, r'$\sigma =${:.2f}'.format(sig.value),fontsize=8)
ax.text(3.,255, r'$N_c =${:}'.format(int(norm.value)),fontsize=8)

#h.plot()
plt.hist(randNum, bins, ec='black', range=(x_min,x_max))
h.plot_exp(color='black')
B.pl.show()
