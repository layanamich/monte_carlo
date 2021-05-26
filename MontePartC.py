

import random
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm

# Helper function 
def Poisson_value(mu):
    r = random.uniform(0, 1)
    values = list()
    for i in range(1000):
        values.append(poisson.pmf(i,mu))
        if sum(values) > r: break
    return  len(values)-1

# Data gen
N = 10000
mu1 = [ Poisson_value(1.0)  for i in range(N)]
mu10_3 =  [ Poisson_value(10.3)  for i in range(N)]
mu102_1 = [ Poisson_value(102.1) for i in range(N)]

# Interpolation

def extract(data):
    counts = dict()
    for i in mu1:
        counts[i] = counts.get(i, 0) + 1
    data = sorted(counts.items())
    x_vals = [ v[0] for v in data ]
    y_vals = [ v[1]/N for v in data ]
    return x_vals , y_vals

### Figure 1
plot1 = plt.figure(1)
data = mu1
x , y = extract(data)
plt.hist(data, density = 1, bins = (max(x)+1), rwidth = 0.85 )

mu , std = norm.fit(data)
p = norm.pdf(range(int(mu-4*std), int(mu+4*std)),mu,std)
plt.plot(range(int(mu-4*std), int(mu+4*std)), p)

plt.xlabel("Values")
plt.ylabel("Probability")
plt.title("Poisson deviates for $\mu=1.0$")
plt.legend(["Fit", "Normalized Data"])

### Figure 2
plot2 = plt.figure(2)
data = mu10_3
x , y = extract(data)
plt.hist(data, density = 1, bins = (max(x)+1), rwidth = 0.85 )

mu , std = norm.fit(data)
p = norm.pdf(range(int(mu-4*std), int(mu+4*std)),mu,std)
plt.plot(range(int(mu-4*std), int(mu+4*std)), p)

plt.xlabel("Values")
plt.ylabel("Probability")
plt.title("Poisson deviates for $\mu=10.3$")
plt.legend(["Normal Fit", "Normalized Data"])

### Figure 3
plot3 = plt.figure(3)
data = mu102_1
x , y = extract(data)
plt.hist(data, density = 1, bins = (max(x)+1), rwidth = 0.85 )

mu , std = norm.fit(data)
p = norm.pdf(range(int(mu-4*std), int(mu+4*std)),mu,std)
plt.plot(range(int(mu-4*std), int(mu+4*std)), p)

plt.xlabel("Values")
plt.ylabel("Probability")
plt.title("Poisson deviates for $\mu=102.1$")
plt.legend(["Normal Fit", "Normalized Data"])


plt.show()