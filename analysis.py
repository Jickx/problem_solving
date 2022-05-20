import time


def find_min_lin(my_list):
	start = time.time()
	min = my_list[0]
	for i in range(len(my_list)):
		if min > my_list[i]:
			min = my_list[i]
	end = time.time()
	return min, end - start

def find_min_quad(my_list):
	start = time.time()
	for i in my_list:
		is_smallest = True
		for j in my_list:
			if i > j:
				is_smallest = False
		if is_smallest:
			smallest_overall = i
	end = time.time()
	return smallest_overall, end-start




print("%d %0.5f" % find_min_lin([2,4,5,-100,2,600,-1000]))
print("%d %0.5f" % find_min_quad([2,4,5,-100,2,600,-1000]))