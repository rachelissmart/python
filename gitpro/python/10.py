def print_none():
 print "Hello world."
def print_one(arg):
 print "I like %r." %arg
def print_two(arg1,arg2):
 print "I like %r and %r." %(arg1,arg2)
print_none()
print_one("apple")
print_two("apple","banana")

def add(a,b):
 return a+b
 
groupA=20
groupB=30
total=add(groupA,groupB)
print "Total is %d." % total
