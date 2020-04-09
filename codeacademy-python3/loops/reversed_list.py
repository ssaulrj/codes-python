#Write your function here
def reversed_list(lst1, lst2):
  if lst1 == lst2[::-1]:
    return True
  else:
    return False
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
