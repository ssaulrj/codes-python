letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  cuenta = 0
  lettersin = []
  for x in letters:
    if word.count(x) > 0:
      if x not in lettersin:
        lettersin.append(x)
        cuenta += 1
  print(lettersin)
  return cuenta

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

"""Output:
['i', 'm', 'p', 's']
4
['A', 'e', 'l', 'p']
4
"""
