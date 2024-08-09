num = int(input("Enter the number: "))
factors = []
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        factors.append(i)
        if i != num // i:
            factors.append(num // i)
factors.sort()
print("The factors are:\n",factors)