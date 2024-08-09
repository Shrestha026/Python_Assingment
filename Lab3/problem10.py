def print_segment_display(n):
	if  n < 0 or n > 9:
		print('Number should be between 0 and 9!')
		return
	if n == 0:
		print(' _ ')
		print('| |')
		print('|_|')
	elif n == 1:
		print('   ')
		print('  |')
		print('  |')
	elif n == 2:
		print(' _ ')
		print(' _|')
		print('|_ ')
	elif n == 3:
		print(' _ ')
		print(' _|')
		print(' _|')
	elif n == 4:
		print('   ')
		print('|_|')
		print('  |')
	elif n == 5:
		print(' _ ')
		print('|_ ')
		print(' _|')
	elif n == 6:
		print(' _ ')
		print('|_ ')
		print('|_|')
	elif n == 7:
		print(' _ ')
		print('  |')
		print('  |')
	elif n == 8:
		print(' _ ')
		print('|_|')
		print('|_|')
	elif n == 9:
		print(' _ ')
		print('|_|')
		print(' _|')


n = int(input('Enter a number between 0 and 9: '))
print_segment_display(n)
