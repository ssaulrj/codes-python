first_name = "Reiko"
last_name = "Matsuki"

#concatenate the last three letters of each and returns them as a string.
def password_generator(first_name, last_name):
  len1 = len(first_name)
  len2 = len(last_name)
  new_string = first_name[len1-3:] + last_name[len2-3:]
  return new_string

temp_password = password_generator(first_name, last_name)
print(temp_password)
