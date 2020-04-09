#This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
  count = word.count(letter)
  if count >= 1:
    return True
  else:
    return False

print(letter_check('saulau', 'aux'))
