students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  students_period_B.append(student)
  print(student)
  
#---------------------------------------------------------------------------

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
  print(breed)
  if breed == dog_breed_I_want:
    print('They have the dog I want!')
    break

#---------------------------------------------------------------------------
 
 ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  else:
    print(i)
 
#---------------------------------------------------------------------------
#Use of pop()

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  x = all_students.pop()
  students_in_poetry.append(x)

print(all_students)
print(students_in_poetry)
 
#---------------------------------------------------------------------------

