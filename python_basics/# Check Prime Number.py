# Check Prime Number

num = int(input("Enter a number: "))
prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not Prime Number")