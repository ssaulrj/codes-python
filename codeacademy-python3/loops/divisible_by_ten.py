#Write your function here
def divisible_by_ten(nums):
  cuenta = 0
  for i in nums:
    if i%10 == 0:
      cuenta += 1
  return cuenta

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
