#Write a function named larger_list that has two parameters named lst1 and lst2.
#The function should return the last element of the list that contains more elements. 
#If both lists are the same size, then return the last element of lst1.

#Write your function here
def larger_list(lst1,lst2):
  element_lst1 = len(lst1)
  element_lst2 = len(lst2)
  if element_lst1 > element_lst2 or element_lst1 == element_lst2:
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10,15]))
