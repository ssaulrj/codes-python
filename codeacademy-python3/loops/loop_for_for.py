#---------------------------------------------------------------------------

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for y in location:
    scoops_sold += y

print(scoops_sold)

#---------------------------------------------------------------------------

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []

for i in heights:
  if i > 161:
    can_ride_coaster.append(i)

print(can_ride_coaster)

#---------------------------------------------------------------------------

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = []

for temperature_in_celsius in celsius:
  temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
  fahrenheit.append(temperature_in_fahrenheit)

print(fahrenheit)

#---------------------------------------------------------------------------

single_digits = range(10)
squares = []
cubes = []

for i in single_digits:
  print(i)
  squares.append(i**2)
  cubes.append(i**3)

print(squares)
print(cubes)

#---------------------------------------------------------------------------
