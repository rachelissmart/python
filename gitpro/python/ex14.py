import numpy as np
from sys import argv
script,c=argv
r=float(c)/(2*np.pi)
if  abs(r-6378)<abs(r-3396):
 print "It's Earth."
else:
 print "It's Mars."
