# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  print(end_index)
  if end_index == -1:
    return word
  else:
    return word[start_index+1:end_index]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
