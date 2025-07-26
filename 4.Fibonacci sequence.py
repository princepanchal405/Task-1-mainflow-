# Fibonacci sequence generator
n = int(input("Enter your number of Fibonacci Number to generator: "))

fibonacci_sqn = []
a, b = 0, 1
for _ in range(n):
    fibonacci_sqn.append(a)
    a, b = b, a+b

print("Fibonacci sequence:")
print(fibonacci_sqn)