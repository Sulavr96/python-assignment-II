def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("The number is prime")
else:
    print("The number is not prime")
