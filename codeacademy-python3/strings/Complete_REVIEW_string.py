highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

#The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.
highlighted_poems_list = highlighted_poems.split(',')
#print(highlighted_poems_list)

highlighted_poems_stripped = []
for i in highlighted_poems_list:
  x = i.strip()
  highlighted_poems_stripped.append(x)
#print(highlighted_poems_stripped)

# break up all the information for each poem into it’s own list, so we end up with a list of lists.
highlighted_poems_details = []
for i in highlighted_poems_stripped:
  x = ''.join(i)
  x = x.split(':')
  #print(x)
  highlighted_poems_details.append(x)
print(highlighted_poems_details)

titles = []
poets = []
dates = []
for i in highlighted_poems_details:
  titles.append(i[0]) #titles
  poets.append(i[1]) #poets
  dates.append(i[2]) #dates

print(titles)
print(poets)
print(dates)

for i in range(len(titles)):
  print('The poem {} was published by {} in {}'.format(titles[i],poets[i],dates[i]))
