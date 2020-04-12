def count_char_x(word, x):
  cuenta = 0
  for xx in range(len(word)):
    if word[xx] == x:
      cuenta += 1
  return cuenta

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
