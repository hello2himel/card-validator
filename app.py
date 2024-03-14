def validate_card(card_number):
    # Remove any spaces and reverse the number
    card_number = card_number.replace(" ", "")[::-1]
    
    # Convert the reversed string to a list of integers
    digits = [int(x) for x in card_number]
    
    # Double every second digit
    doubled_digits = [(2 * digit) if index % 2 != 0 else digit for index, digit in enumerate(digits)]
    
    # Subtract 9 from numbers over 9
    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
    
    # Calculate the sum of all digits
    total_sum = sum(subtracted_digits)
    
    # Check if the sum is divisible by 10
    return total_sum % 10 == 0

# Test the function
card_number = input("Enter your credit/debit card number: ")
if validate_card(card_number):
    print("Valid card number.")
else:
    print("Invalid card number.")
