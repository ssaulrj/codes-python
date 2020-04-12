# Write your reverse_string function here:
def reverse_string(word):
  lst = []
  for i in word:
    lst.append(i)
  lst.reverse()
  string_new = ''.join(lst)
  return string_new

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
