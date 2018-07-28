#ex12.1
a=[1,2,4,4,53,2,4,3,2,3,"c","a"]
b=(3,"b")
c=range(20)
print a
print b
print c

print c[0]*b[0]
print a[1]/c[2]

#ex12.2
del c[0:6:2]
print c
a.append(27)
print a
del c[1:3]
print c
c.insert(3,4)
print c
c.remove(4)
print c
c.reverse()
print c
c*=3
print c

#ex12.3
a[1]=1
print a


