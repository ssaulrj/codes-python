heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15],['Dhruti', 16]]

#------------------------------------------------------------------------------
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

#Zip command to join list part x(0) with part y(0), etc 
names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
#------------------------------------------------------------------------------
orders = ['daisies', 'periwinkle']
print(orders)

#append() : add a element to a list
orders.append('tulips')
orders.append('roses')
print(orders)
#------------------------------------------------------------------------------
list1 = range(5, 15, 3)
list2 = range(0, 40, 5)

first_names = ['Ainsley','Ben','Chani','Depak']

age = []
age.append(42)
all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)

print(list(name_and_age))
ids = range (4)
#------------------------------------------------------------------------------
