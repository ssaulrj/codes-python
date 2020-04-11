dict = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

#Alter
dict['gato'] = 'minou'
print(dict)

#Add
dict['cisne'] = 'cygne'
print(dict)

#Update
dict.update({"pato" : "canard"})
print(dict)

#Delete
del dict['caballo']
print(dict)

#Delete last element
dict.popitem()
print(dict) 
