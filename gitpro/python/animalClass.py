class organism(object):
 def __init__(self):
  self.can_die=True
  self.propogation=True
 def pp1(self):#properties1
  print "-Can die.\n -Can propogate.\n"
 
  
class animal(organism):
 def __init__(self):
  super(animal,self).__init__()
  self.can_move=True
  self.dont_need_water=False
 def pp2(self):#properties2
  print "-Can move.\n -Water is neccessary for them.\n"
       
class vertebrate(animal):
 def __init__(self):
   super(vertebrate,self).__init__()
  self.have_vertebration=True
  self.is_monad=False
 def pp3(self):#properties3
  print "-Have vertebration.\n -They're monad.\n"
class mammal(vertebrate):
 def __init__(self):
  super(mammal,self).__init__()
  self.breed_baby_with_breast=True
  self.give_birth_to_eggs=False
 def pp4(self):#properties4
  print "-They breed babies with breast.\n -They give birth to eggs.\n"
class dog(mammal):
 def which_dog(self):
  super(dog,self).__init__()
 def owner(self):
  if self=="Rover":
   print "This dog belongs to Me."
  elif self=="Dick":
   print "This dog belongs to Richard."
  
  
  

         
rover=dog()
rover.name='Rover'
rover.owner='ME'
