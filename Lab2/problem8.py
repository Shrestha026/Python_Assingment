def power(num, pow):
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        return num * power(num, pow - 1)
    
print(power(10,2))