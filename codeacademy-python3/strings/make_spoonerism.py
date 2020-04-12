# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  word1x, word2x = [], []
  for i in word1:
    word1x.append(i)
  for i in word2:
    word2x.append(i)
  aux = word1x[:]
  word1x[0] = word2x[0]
  word2x[0] = aux[0]
  strnew = ''.join(word1x) + ' ' + ''.join(word2x) 
  return strnew

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
