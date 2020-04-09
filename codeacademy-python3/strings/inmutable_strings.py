first_name = "Bob"
last_name = "Daily"

#This is a error, Strings are inmutable
#first_name[0] = "R"

#Concatenate the string "R" with a slice of first_name that includes everything but the first character
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
