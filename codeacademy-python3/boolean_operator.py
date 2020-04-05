not True == False
not False == True

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2.0 :
    return "You meet the requirements to graduate!"
    
def graduation_reqs2(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if gpa >= 2.0 and credits<120:
    return "You do not have enough credits to graduate."
  if gpa < 2.0 and credits>=120:
    return "Your GPA is not high enough to graduate."
  if gpa < 2.0 and credits<120:
    return "You do not meet either requirement to graduate!"
