
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

limit = int(input("Enter the limit: "))

for i in range(2, limit+1):
    if is_prime(i):
        print(i, end=" ")

