num= int(input("Enter a positive integer number: "))

for num in range(2, num+ 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

else:
    print("Please enter a positive integer.")

 