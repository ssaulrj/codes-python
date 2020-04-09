#Write your function here
def over_nine_thousand(lst):
  if len(lst) != 0:
    sum = 0
    for i in lst:
      if sum > 9000: 
        return sum
      else:
        sum += i
    return sum
  else:
    return 0

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
