import timeit
import random

def del_dict_items(x):
# Insert the index
    random_index = random.randrange(len(x) - 1)
    try:
        del x[random_index]
    except KeyError:
        x.setdefault(random_index, None)
        del x[random_index]

print("i\t\tlist_del_time\t\tdict_del_time")
for i in range(10000, 1000000, 20000):
    t_list = timeit.Timer("del x[random.randrange(len(x)-1)]", "from __main__ import random, x")
    t_dict = timeit.Timer("del_dict_items(x)", "from __main__ import random, x, del_dict_items")
    x = list(range(i))
    list_del_time = t_list.timeit(number=1000)
    x = {j:None for j in range(i)}
    dict_del_time = t_dict.timeit(number=1000)
    print("%d %15.4f %23.4f" %(i, list_del_time, dict_del_time))