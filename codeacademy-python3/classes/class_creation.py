class Facade:
  pass

#Create an instance of our defined Facade
facade_1 = Facade()

#Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.
facade_1_type = type(facade_1)
print(facade_1_type)
#In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”

#-------------------------------------------- class variable
class Grade:
  minimum_passing = 65
  
#-------------------------------------------- class and methods
class Rules:
  
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
