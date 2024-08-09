def calculate_series(x, n):
	sum = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			sum -= x**(2*i-1)/factorial(2*i-1)
		else:
			sum += x**(2*i-1)/factorial(2*i-1)
	return sum

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

x = int(input('Enter x: '))
n = int(input('Enter a positive integer: '))
print(round(calculate_series(x, n),4))
