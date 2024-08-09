def factorial(n):
    return (1 if n == 0 else  n * factorial(n-1))

def is_krishnamurthy(num):
    original_num, sum = num, 0
    while num > 0:
        sum += factorial(num % 10)
        num //= 10
    return sum == original_num

num = int(input("Enter a number: "))
if is_krishnamurthy(num):
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")