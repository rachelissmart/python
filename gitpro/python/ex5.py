#EX5
import numpy as np
r=6378*1000
c=2*np.pi*r
s=4*np.pi*r*r
data="Earth equator:\n\t*circumference: %f m \n\t*surface: %f m^2" %(c,s)
print data

#input 1
print "What's your name?"
name=raw_input()
print "How old are you?"
age=raw_input()
print "My name is %s and I am %s years old."%(name,age)
#input 2
name=raw_input("What's your name?")
age=raw_input("How old are you?")
print "My name is %s and I am %s years old."%(name,age)
