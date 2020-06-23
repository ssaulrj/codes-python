def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

#In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

#Pprint the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))
    
#Script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
for x in range(0,101):
    if x%7 == 0:
        print(x)

#The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. Currently the code will keep executing the function even if it succeeds. The code stops trying after the operation succeeded.
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
