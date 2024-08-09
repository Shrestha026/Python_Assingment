def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

def is_armstromg(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return sum == num



if __name__ == "__main__":
    num = int(input("Enter a number:   "))

    if is_perfect(num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

    if is_armstromg(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")


