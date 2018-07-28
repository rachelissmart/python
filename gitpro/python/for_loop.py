#read dicts
f=['a','b','c']
g={'a':1,'b':2,'c':3}
for i in f:
 print g[i]

a=(1,2,3)
for  i in a :
 print i
print 1+3

b={1,2,3}
c={1:'a',2:'b',3:'c'}
for i in b:
 print c[i]
 
d=range(11)
e=[];
for i in d:
 e.append((1+0.1*i)**(1+0.1*i))
 print e[i]
