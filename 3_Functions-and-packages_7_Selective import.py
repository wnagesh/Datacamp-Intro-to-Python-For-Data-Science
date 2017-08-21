# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
phi=radians(12)
dist=r*phi

# Print out dist
print(dist)