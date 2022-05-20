import timeit
import random

for i in range(100000, 1000000, 20000):
    index = timeit.Timer(f"l[random.randrange({i})]",
                         "from __main__ import random, l")
    l = list(range(i))
    index_time = index.timeit(number = 1000)
    print(f"{l}, {index_time:0.5f}")
    