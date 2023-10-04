# Input a 5-digit number as a string
number_str = input("Enter a 5-digit number: ")

# Check if the input has exactly 5 digits
if len(number_str) != 5 or not number_str.isdigit():
    print("Please enter a valid 5-digit number.")
else:
    # Convert the string to an integer
    number = int(number_str)

    # Calculate the sum of digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10

    print("Sum of digits:", digit_sum)

