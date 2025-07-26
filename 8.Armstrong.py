# armstrong number check

num = int(input("Enter a number: "))

num_str = str(num)
power = len(num_str)

total = sum(int(digit) ** power for digit in num_str)

armstrong = total == num
print("Armstrong number?", armstrong)