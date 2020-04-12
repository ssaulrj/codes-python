# Write your add_exclamation function here:
def add_exclamation(word):
  lst = []
  for i in word:
    lst.append(i)
  len_lst = len(lst)
  if len_lst >= 20:
    return word  
  else:
    while len(lst) < 20:
      lst.append("!")
    return ''.join(lst)  

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
