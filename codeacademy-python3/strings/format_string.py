#.format(), why is this method better? The answer is legibility and reusability. It is much easier to picture the end result .format() than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same base string with different variables, allowing you to cut down on unnecessary, hard to interpret code.
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))


def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {} by {} was originally published in {} in {}.".format(title, author, original_work, publishing_date)
  return poem_desc

my_beard_description = poem_description('1974', 'Shel Silverstein', 'My Beard', 'Where the Sidewalk Ends')
