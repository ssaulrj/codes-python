# Write your sum_values function here:
def sum_values(my_dictionary):
  sumx = 0
  for x in my_dictionary.values():
    sumx += x
  return sumx
  
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
