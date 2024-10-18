# Define word lists for numbers
ones = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

thousands = ["", "thousand", "million", "billion"]

# Get user input
number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please enter a positive integer.")
else:
    words = ""
    if number == 0:
        words = "zero"
    else:
        for i in range(len(thousands)):
            chunk = number % 1000
            if chunk > 0:
                words_chunk = ""
                if chunk >= 100:
                    words_chunk += ones[chunk // 100] + " hundred "
                    chunk %= 100
                
                if chunk >= 20:
                    words_chunk += tens[chunk // 10] + " "
                    chunk %= 10
                
                if chunk > 0:
                    words_chunk += ones[chunk] + " "
                
                words = words_chunk.strip() + " " + thousands[i] + " " + words
            
            number //= 1000

    print(f"The number in words is: {words.strip()}")
