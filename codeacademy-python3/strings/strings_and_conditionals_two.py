def contains(big_string, little_string):
  if (little_string in big_string) == True:
    return True
  else:
    return False

def common_letters(string_one, string_two):
  share_letters = []
  len1 = len(string_one)
  for i in range(len1):
    if (string_one[i] in string_two) == True:
      if (string_one[i] in share_letters) == False:
        share_letters.append(string_one[i])
  return share_letters

#takes two arguments, big_string and little_string and returns True if big_string contains little_string.
print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))

#Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
print(common_letters("banana", "cream"))
print(common_letters('python', 'ruby on rails'))
