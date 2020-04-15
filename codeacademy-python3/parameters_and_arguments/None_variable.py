#None is a special value in Python. It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).
#None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. None is also unique, which means that you can test if something is None using the is keyword.

from review_lib import get_next_review, submit_review

# define review here!
review = get_next_review()

if review == None:
  pass
else: 
  submit_review(review)
