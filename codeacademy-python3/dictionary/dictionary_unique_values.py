# Write your unique_values function here:
def unique_values(my_dictionary):
  list = []
  for y in my_dictionary.values():
    if y not in list:
      list.append(y)
  return len(list)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
