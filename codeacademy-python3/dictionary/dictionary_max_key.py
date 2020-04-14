# Write your max_key function here:
def max_key(my_dictionary):
  list_num = []
  for x in my_dictionary.values():
    list_num.append(x)
  maxnum = max(list_num)
  for x in my_dictionary:
    if maxnum == my_dictionary[x]:
      return x
      
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
