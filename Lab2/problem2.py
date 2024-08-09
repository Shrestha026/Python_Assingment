a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

disc = b**2 - 4*a*c
if disc < 0:
    print("The equation has no real roots.")
elif disc == 0:
    r = -b/(2*a)
    print("The root is", r)
else:
    r1 = (-b + disc**0.5)/(2*a)
    r2 = (-b - disc**0.5)/(2*a)
    print("The roots are", r1, "and", r2)