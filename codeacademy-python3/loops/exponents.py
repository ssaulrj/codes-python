#Write your function here
def exponents(bases, powers):
  raised = []
  for i in bases:
    for ii in powers:
      raised.append(i**ii)
  return raised

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
