def is_positive(number):
  if number > 0:
    return True
  else:
    return None
    
def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    print("Full_blocks "+str(full_blocks))
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    print("Partial_block_remainder "+str(partial_block_remainder))
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return 4096*full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def format_name(first_name, last_name):
	# code goes here
	if len(first_name) > 0 and len(last_name) > 0:
		string = "Name: "+last_name+", "+first_name
	elif len(first_name) == 0 and len(last_name) > 0:
		string = "Name: "+last_name
	elif len(first_name) > 0 and len(last_name) == 0:
		string = "Name: "+first_name
	else:
		string = ""
	return string 

print(format_name("Ernest", "Hemingway")) # Should return the string "Name: Hemingway, Ernest"
print(format_name("", "Madonna")) # Should return the string "Name: Madonna"
print(format_name("Voltaire", "")) # Should return the string "Name: Voltaire"
print(format_name("", "")) # Should return an empty string

#The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length).
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

#The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	# keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	result = numerator / denominator
	resultnumber = result % 1
	return resultnumber

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
