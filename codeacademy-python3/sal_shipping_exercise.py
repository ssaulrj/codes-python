premium_ground = 125.00 

def groundshipping(weight):
  cost = 0
  if weight <= 2:
     cost = weight * 1.50 + 20
  elif weight >2 and weight<=6:
    cost = weight * 3.00 + 20
  elif weight >6 and weight<=10:
    cost = weight * 4.00 + 20
  else: 
    cost = weight * 4.75 + 20
  return cost

def droneshipping(weight):
  cost = 0
  if weight <= 2:
     cost = weight * 4.50
  elif weight >2 and weight<=6:
    cost = weight * 9.00
  elif weight >6 and weight<=10:
    cost = weight * 12.00
  else: 
    cost = weight * 14.25
  return cost

def check(weight):
  cost_ground = groundshipping(weight_package)
  cost_drone = droneshipping(weight_package)
  if cost_ground < cost_drone and cost_ground < premium_ground:
    print("Best: cost_ground and cost "+str(cost_ground))
  elif cost_drone < cost_ground and cost_drone < premium_ground:
    print("Best cost_drone and cost "+str(cost_drone))
  elif premium_ground < cost_ground and premium_ground < cost_drone:
    print("Best premium_ground and cost "+str(premium_ground))

weight_package = 4.8
check (weight_package)
