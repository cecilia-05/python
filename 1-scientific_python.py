import random
from time import perf_counter

import numpy as np

print(perf_counter(), "Generating numbers...")

# slowest possible version
numbers = []
for _ in range(50_000_000):
    n = np.random.random()
    numbers.append(n)

# numpy version 1
numbers = np.zeros(shape=(50_000_000))
for i in range(50_000_000):
    n = np.random.random()
    numbers[i] = n

# Best numpy version
numbers = np.random.random(50_000_000)

# Pure Python version
#numbers = []
#for i in range(10_000_000):
#    if i % 10_000_000 == 0:
#        print(perf_counter(), "Generated", i, "...")
#    n = random.random()
#    numbers.append(n)


print(perf_counter(), "Finisheed generating.")

