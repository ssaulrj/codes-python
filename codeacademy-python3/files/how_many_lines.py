with open('how_many_lines.txt') as lines_doc:
  #lines_docx = lines_doc.read()
  for line in lines_doc.readlines():
    print(line)

#print(lines_docx)
