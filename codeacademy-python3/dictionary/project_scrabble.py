#Dictionaries--------------------------------------------
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

player_to_words = {"player1":["BLUE","TENNIS","EXIT"],
                   "wordNerd":["EARTH", "EYES", "MACHINE"],
                   "Lexi Con":["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader":["ZAP", "COMA", "PERIOD"],
                  }

#--------------------------------------------------------
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for x in word:
    point_total += letter_to_points.get(str(x), 0) 
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

#--------------------------------------------------------
player_to_points = {}
player_points = 0
for key, value in player_to_words.items():
  player_points = 0
  for word in value:
    print(word)
    player_points += score_word(str(word))
  player_to_points[str(key)] = player_points
print(player_to_points)

"""
If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well
"""
