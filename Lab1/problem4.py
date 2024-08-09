num= int (input("Enter a number: "))
rev = 0
while num:
    rev = rev*10 + num%10
    num //= 10
print("The reverse number is: ",rev)