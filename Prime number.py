def prime_number(n):
    if number < 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n% i ==0:
            return  False
    return True
number = int(input("Enter the number: "))
print(prime_number(number))

