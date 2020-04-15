how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for x in how_many_s:
  x_count = hasattr(x, "count")
  #print(x_count)
  if x_count == True:
    num_s = x.count("s")
    print(num_s)
