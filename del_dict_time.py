import timeit
import random

for i in range(10000, 1000000, 20000):
    t_dict = timeit.Timer("del x_copy[random.randrange(i)]", "from __main__ import random, x_copy, i")

    dict_del_time = {}
    del_time = 0
    x = {j:None for j in range(i)}

    for j in range(1000):
        x_copy = x.copy()
        del_time += t_dict.timeit(number=1)
    dict_del_time[i] = round(del_time, 6)
              
    print(f"{dict_del_time}")