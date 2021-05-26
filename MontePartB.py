
'''An object at the origin of n-dimensional space'''


from numpy import random
import numpy as np
import copy
from scipy.special import gamma

# Radius of sphere
r = 1.0
# Where n is an array containing dimensions
n = [1,2,3,4,5]
#Volume of spheres ( Theoretical)
V_SphereTheo = []
# Number of Interaction
N = 10000
# Demensions of Box/Sphere
dim =n[0]

''' Returns the theoretical volume of a sphere for a given dimmension n and radius r '''
def SphereVolume(n,r):
     V= np.pi**(n/2.)*r**n/gamma(n/2.+1.)
     return V
for i in range(len(n)):
    V_SphereTheo.append(SphereVolume(n[i],r))
    print("The theoretical volume of a {:} dimensional sphere is: {:}"\
          .format(n[i],V_SphereTheo[i])) 

from Particle import particle

# Main Outer Loop running on n
for i_n in range(len(n)): 
    # Initialize points in Box (Total point thrown) Index
    i_B = 0
    # Initialize points in Sphere Index
    i_S = 0
    # Loop Throwing N points
    for i_B in range(N+1): 
        # Initialize point
        p = particle() 
        p.setDim(dim)
        # Initialize Length
        L = 0 
         # Throw point
    for i_n in range(dim):
        # random coordinate from [-r,r]
        p.box_x[i_n] = random.uniform(-r, r) 
        L += p.box_x[i_n]**2
 # Distance of points from Origin 
    L = np.sqrt(L) 
    if (L < 1.0):
         # Add Points to sphere array
        p.sphere_x = copy.copy(p.box_x)
        i_S += 1
i_S -= 1

     

        
print("\ n For a {:} dimensional sphere".format(dim))
print("The number of points thrown : {:}".format(i_B))
print("The number of points in the sphere: {:}".format(i_S))

# Volume of Box
V_B = (2.*r)**dim 
V_SphereExper = V_B*i_S/i_B
dV_SphereExper = V_B*i_S/i_B*np.sqrt(1./i_S + 1./i_B)

print("The approximate volume of the sphere: {:.3f} +/- {:.3f}".\
format(V_SphereExper, dV_SphereExper))
print("The relative uncertainty is: {:.5f} %".\
format(100.*dV_SphereExper/V_SphereExper))
dim += 1
