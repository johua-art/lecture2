def are_anagrams(str1, str2):
    # Normalize the strings: remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "enlist"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
