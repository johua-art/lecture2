def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in input_string if char not in vowels])

user_input = input("Enter a string: ")
result = remove_vowels(user_input)

# Display the result
print("String without vowels:", result)
