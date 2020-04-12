#---------------------------------------------------------------------------------------------------------
#We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.
#Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#{key:value for key, value in zip}
plays = {song:playcount for song, playcount in zip(songs,playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays ,"Sunday Feelings":{}}
print(library)
