class organism(object):
 def __init__(self):
  self.can_die=True
  self.propogation=True
 def ppt1(self):#properties1
  print "As an organism \n\t-They can die.\n\t-They can propogate.\n"
 
  
class animal(organism):
 def __init__(self):
  super(animal,self).__init__()
  self.can_move=True
  self.dont_need_water=False
 def ppt2(self):#properties2
  print "As an animal \n\t-They can move.\n\t-Water is neccessary for them.\n"
       
class vertebrate(animal):
 def __init__(self):
  super(vertebrate,self).__init__()
  self.have_vertebration=True
  self.is_monad=False
 def ppt3(self):#properties3
  print "As a vertebrate \n\t-They have vertebration.\n\t-They're monad.\n"
class mammal(vertebrate):
 def __init__(self):
  super(mammal,self).__init__()
  self.breed_baby_with_breast=True
  self.give_birth_to_eggs=False
 def ppt4(self):#properties4
  print "As a mammal \n\t-They breed babies with breast.\n\t-They give birth to eggs.\n"
class dog(mammal):
 def __init__(self):
  super(dog,self).__init__()
 def ppt5(self):#properties5
  print "As a dog \n\t-They bark a lot.\n\t-Rover belongs to me while Richard belongs to Richard."
  
