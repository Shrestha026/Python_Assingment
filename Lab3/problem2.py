def calculate_slope(x1, y1, x2, y2):
	return (y2 - y1) / (x2 - x1)

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
print("The slope of the given parameter is: ",calculate_slope(x1, y1, x2, y2))