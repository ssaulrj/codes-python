import codecademylib3_seaborn
from matplotlib import pyplot as plt 
import random

# Add your code below:
numbers_a = range(1,13)
#numbers_b = [random.randint(1,13) for i in range(1000)]
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()
