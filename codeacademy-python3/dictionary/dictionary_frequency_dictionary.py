# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  dic = {}
  for x in words:
    num = words.count(x)
    dic[x] = num
  return dic

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
