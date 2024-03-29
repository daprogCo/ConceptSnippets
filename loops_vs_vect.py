"""
### Example of vectorization in Python ###

Vectorization is the process of converting an algorithm from operating on a single value at a time to operating on a set of values (vector) at one time. This is done by using libraries like NumPy that provide support for vectorized operations.

In this example, we compare the performance of iterative sum and vectorized sum using NumPy for a large number of elements.

The gain in performance is due to the fact that NumPy uses optimized C code to perform the operations on the entire array at once, rather than looping over each element individually.
"""

import pandas as pd
import numpy as np
import time

# Test the performance of iterative sum
start = time.time()
total = 0
for item in range(0, 1500000):
    total = total + item
print('sum is:' + str(total))
end = time.time()
print('loop1: ', end - start)

# Test the performance of vectorized sum
start = time.time()
# .sum() is a vectorized operation from numpy that sums all the elements in the array created using .arange()
sum1 = np.sum(np.arange(1500000, dtype=np.int64))
print('sum is: ', sum1)
end = time.time()
print('vect1: ', end - start)

# Create a large pandas dataframe
df = pd.DataFrame(np.random.randint(1, 50, size=(5000000, 4)),
                  columns=('a', 'b', 'c', 'd'))

# Test the performance of iterative operation to calculate the ratio
start = time.time()
df["ratio"] = 100 * (df["d"] / df["c"])
end = time.time()
print('loop2: ', end - start)

# Test the performance of vectorized operation to calculate the ratio
# The vectorized operation is faster than the iterative operation and format the output in an visually nice comprehensible way
start = time.time()
print(df.head())
end = time.time()
print('vect2: ', end - start)