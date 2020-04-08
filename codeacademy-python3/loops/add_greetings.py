#Write your function here
def add_greetings(names):
  new_list = []
  for i in names:
    new_list.append("Hello, "+i)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
