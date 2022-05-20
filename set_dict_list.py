import timeit
import random

for i in range(10000, 1000000, 20000):
    set_dict = timeit.Timer(f"my_dict[{random.randrange(i)}] = None", 
                     "from __main__ import random, my_dict")
    get_time = timeit.Timer(f"my_dict[{random.randrange(i)}]",
                            "from __main__ import random, my_dict")

    my_dict = {j:None for j in range(i)}
    set_time = set_dict.timeit(number=1000)
    get_time = get_time.timeit(number=1000)

    print(f"set: {i}, {set_time:0.6f}")
    print(f"get: {i}, {get_time:0.6f}")