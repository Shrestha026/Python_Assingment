def reverse_list(lst):
	rev = []
	for i in range(-1, -len(lst), -1):
		rev.append(lst[i])
	return rev

lst = [eval(e) for e in input('Enter a list of numbers separated by space: ').split()]
print(reverse_list(lst))