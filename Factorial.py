def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Input from user
num = int(input("Enter a number: "))

# Display result
print(f"Factorial of {num} is {factorial(num)}")
