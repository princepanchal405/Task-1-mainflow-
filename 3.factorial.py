# Factorial using loop
n = int(input("Enter your number: "))
fact = 1 

if n < 0:
    print("Factorial is not defind for negative numbers.")
else:
    for i in range(1, n+1):
        fact *= i
    print("Factorial of",n, "is", fact)