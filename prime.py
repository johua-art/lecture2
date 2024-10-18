
    





def is_palindrome():
    user_input = input("Please enter a string: ")
    # Normalize the string
    normalized_input = user_input.replace(" ", "").lower()
    return normalized_input == normalized_input[::-1]

# Call the function 
if is_palindrome():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
