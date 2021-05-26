
# Experiment 01  Calculating the value of pi using Monte Carlo methods
'''
Inscribe circle into a square centered at the origin
A_c = pi*r^2
A_s = L*W = (2r)(2r) = 4r^2
(A_c/A_s) = (pi*r^2)/(4*r^2) = pi/4
pi = 4*A_c/A_s = 4*N_c/N_s
N_c <= N_s
'''
#%matplotlib
# Section A of Monte Carlo Lab
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import math

#storing vslues of pi
pi_values =[]

for i in range(1, 500):

#Number of dots 
    N= 1000
#circle coordinates
    circle_x =[]
    circle_y=[]
# Square Coordinates 
    square_x = [] 
    square_y = []
# Initialize Index
    j = 1
# create randomized (x,y) values from [-1, 1]
    while j <= N:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2 <= 1.0):
            circle_x.append(x)
            circle_y.append(y)
        else:
            square_x.append(x)
            square_y.append(y)
        j += 1
    
    pi = 4.0*len(circle_x)/float(N)

#Append the values of pi in list
    pi_values.append(pi)

#Calculatiing the errors
    avg_pi_errors = [abs(math.pi - pi) for pi in pi_values]

#Print the final value of Pi for each run
print (pi_values[-1])
print (avg_pi_errors[-1])
#Plot the Pi values
plt.axhline(y=math.pi, color='g', linestyle='-')
plt.plot(pi_values)
plt.ylim(2, 4)
plt.xlabel("Interations")
plt.ylabel("Value of Pi")
plt.show()
     

#Plot the error in the calculation
plt.axhline(y=0.0, color="g", linestyle="-")
plt.plot(avg_pi_errors)
plt.xlabel("Interations")
plt.ylabel("Error")
plt.show()


# Ploting circle and square

plt.plot(circle_x,circle_y, 'r.')
plt.plot(square_x, square_y, 'b.')
plt.grid()
plt.show()


N = float(N)
p = len(circle_x)/N
mu = N*p
s = np.sqrt(N*p*(1-p))
'''
dpi/pi = s/mu
dpi = pi*s/mu 
'''
# Counts in Square
Ns = N 
# Counts in Circle
Nc = len(circle_x) 

#dpi = pi*s/mu
#dpi2 = 4.*np.sqrt(Nc*(1.-Nc/Ns))/Ns # Double Checking Pi Error

dpi=pi*np.sqrt((1./Nc + 1./Ns))


print("Pi is approximately : {:5.4f} +/- {:5.4f} ".format(pi,dpi))
print("Pi actually is :", np.pi)
print("The relative uncertainty is: {:.5f} %".format(100.*dpi/pi))

# Desired Relative Uncertainty [%]
e = [1.,0.1, 0.01, 0.00001] 


#Ne = (4.-np.pi)*(1./np.pi)*(100./e[i])**2 
# Approximate Number of events


for j in range(len(e)):

    Ne = (4.+np.pi)*(1./np.pi)*(100./e[j])**2 
    
    print("Events required to obtain a statistical uncertainty\n\
of {:.5} % is: {:} +/- {:}".format(e[j],int(Ne),np.sqrt(int(Ne))))
    print("Events required to obtain a statistical uncertainty\ n \
of {:.5} % is: {:} +/- {:}".format(e[j],int(Ne),np.sqrt(int(Ne))))




