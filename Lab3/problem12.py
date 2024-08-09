def print_table():
	for i in range(1, 6):
		print(i,1, end=' ')
		for j in range(1, 4):
			print(i**j, end=' ')
		print()

print_table()