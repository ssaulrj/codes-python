authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')

def last_names(author_names):
  listx = []
  for i in author_names:
    x = i.split()
    listx.append(x[-1])
  return listx

print(author_names)
#Create another list called author_last_names that only contains the last names of the poets in the provided string.
author_last_names = last_names(author_names)
print(author_last_names)
