#ex10.1
def difference(x1,x2):
 return x1-x2
#x1=raw_input("please input your first float")
#x2=raw_input("please input your second float")
d=difference(3.232332,5.232423)
print "the difference between two floats is %f." %d

#ex10.2
import numpy as np
def circumference(r):
 return 2*np.pi*r*1000
c=circumference(6378)
print "earth's circumference is %f m." %c

#ex10.3
c=circumference(3396)
print "earth's circumference is %f m." %c

