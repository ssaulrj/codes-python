import csv
import json

#---------------------------------------------------------
compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])
print(compromised_users)

#---------------------------------------------------------
#Open this file in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
  for x_users in compromised_users:
    print(x_users)
    compromised_user_file.write(x_users)
compromised_user_file.close() 

with open('compromised_users.txt') as r_users:
  r_csv = r_users.readlines()
  for f_csv in r_csv:
    print(f_csv)

#---------------------------------------------------------
boss_message_dict = {
  'recipient': 'The boss',
  'message': 'Mission Success'
}
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = json.dump(boss_message_dict, boss_message)

#---------------------------------------------------------
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
with open('new_passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)
