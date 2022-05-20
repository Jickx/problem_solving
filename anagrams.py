def check_if_anagram(s1, s2):
	l1 = list(s1)
	l2 = list(s2)

	l1.sort()
	l2.sort()

	print(l1, l2)

	if l1 == l2:
		return True
	else:
		return False


print(check_if_anagram('abcde', 'edcab'))

