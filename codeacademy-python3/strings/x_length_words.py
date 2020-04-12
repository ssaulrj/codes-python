#x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

# Write your x_length_words function here:
def x_length_words(sentence, x):
  xwords = sentence.split()
  for i in xwords:
    if len(i) >= 2:
      pass
    else:
      return False
  return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
