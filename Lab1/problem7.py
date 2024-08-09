def is_staisfy(num):
    if num % 7 == 0 and num % 5 != 0:
        return True
    return False

print("The numbers are:")
for i in range(1000, 2001):
    if is_staisfy(i):
        print(i, end=" ")