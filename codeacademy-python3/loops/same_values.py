#Write your function here
def same_values(lst1, lst2):
  same_values_num = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      same_values_num.append(i)
  return same_values_num
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
