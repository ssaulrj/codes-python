with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  sec_line = first_line_doc.readline()
print(first_line)
print(sec_line)

with open('bad_bands.txt','w') as bad_bands_doc:
  bad_bands_doc.write('catolic')
  
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')
