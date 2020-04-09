#The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.
def username_generator(first_name, last_name):
  if len(first_name) < 3 and len(last_name) >= 4:
    username = first_name + last_name[:4]
  elif len(first_name) >= 3 and len(last_name) < 4:
    username = first_name[:3] + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

#The function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.
def password_generator(username):
  password = username[-1] + username[:-1]
  #for i in range(len(username))
  return password

username = username_generator('saul','juarez')
print(username)

password = password_generator(username)
print(password)
