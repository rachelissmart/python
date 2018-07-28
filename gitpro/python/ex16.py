# 1.type "I love you!" for 521 times
i=1
while i<522:
 print "I love you!"
 i=i+1



# 2.A WHILE that can't be replaced by FOR
import numpy as np
i=0.8
k=0
while i>0.2:
 print i
 print "It's bigger than 0.2!"
 i=np.random.rand(1)
 k=k+1
print k
