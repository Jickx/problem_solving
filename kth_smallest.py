import random

def find_smallest(random_list, k):
    min_list = []
    while len(min_list) < k:
        for i in range(len(random_list)):
            min = random_list[0]
            index = 0
            for i in range(len(random_list)):
                if min > random_list[i]:
                    min = random_list[i]
                    index = i
            min_list.append(min)
            random_list.pop(index)
            if len(min_list) >= k:
                return min_list[k-1]

random_list = [random.randrange(100) for i in range(10)]
print(sorted(random_list))

print(find_smallest(random_list, 4))
