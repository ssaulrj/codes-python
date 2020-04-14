#--------------------------------------------------------
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
  close_this_file.close()

print(setup)

with open('logger.csv') as log_csv_file:
  filex = log_csv_file.read()
print(filex)

#--------------------------------------------------------
import csv

list_of_email_addresses = []
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])
    
#--------------------------------------------------------
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
