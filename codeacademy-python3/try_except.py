def raises_value_error():
  try:
    raise ValueError
  except ValueError:
    print("You raised a ValueError!")
  

raises_value_error()
