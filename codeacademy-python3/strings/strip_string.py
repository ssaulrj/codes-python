love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# Stripping a string removes all whitespace characters from the beginning and end. Consider the following example:
love_maybe_lines_stripped = []
for i in love_maybe_lines:
  x = i.strip()
  print(x)
  love_maybe_lines_stripped.append(x)

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
