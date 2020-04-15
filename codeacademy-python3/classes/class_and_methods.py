class Circle:
  #class variable
  pi = 3.14

  def area(self, radius):
    return self.pi * radius ** 2


#Instance of Circle
circle = Circle()

#A medium pizza that is 12 inches across.
pizza_area = circle.area(12/2)
#Your teaching table which is 36 inches across.
teaching_table_area = circle.area(36/2)
#The Round Room auditorium, which is 11,460 inches across.
round_room_area = circle.area(11460/2)
