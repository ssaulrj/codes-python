class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyers):
    return lawyers in self.lawyers

    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

print(d_and_p.__len__())
print(d_and_p.__contains__("Hi"))
print(d_and_p.__contains__("Donelli"))

"""
Output:
2
False
True
"""
