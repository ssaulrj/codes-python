user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.get("stamina grains")

x = available_items.pop("stamina grains",0)
if x == 0:
  health_points += 0

health_points += available_items.get("power stew")

y = available_items.pop("power stew",0)
if y == 0:
  health_points += 0

health_points += available_items.get("mystic bread", 0)
z = available_items.pop("mystic bread",0)
if z == 0:
  health_points += 0

print(available_items)
print(health_points)
