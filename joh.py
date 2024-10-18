def is_perfect_number(n):
    if n < 1:
        return False  # Perfect numbers are positive integers
    
    # Calculate the sum of proper divisors
    sum_of_divisors = 0
    for i in range(1, 1000000 // 2):
        if n % i == 0:
            sum_of_divisors += i
            
    return sum_of_divisors == n

# Example usage
number = int(input("Enter a positive integer: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
