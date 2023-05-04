import numpy as nb

p0 = 0.4
p1 = 0.6

c0 = 3
c1 = 8

var = c0*p0+c1*p1

aux1 = (c1-c0)/var
aux2 = (c0**2-c1**2)/(2*var)
#print(var)

threshold1 = ((nb.log(p0/p1))-(c0**2-c1**2)/(2*var))/((c1-c0)/var)

threshold = ((var/(c1-c0))*nb.log(p0/p1))+((c0+c1)/2)
print(threshold)
print(threshold1)