#Write your function here
def larger_sum(lst1, lst2):
  var1, var2 = 0, 0
  for i in lst1:
    var1 += i
  for ii in lst2:
    var2 += ii
  print(var1)
  print(var2)
  if var1 > var2 or var1 == var2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
