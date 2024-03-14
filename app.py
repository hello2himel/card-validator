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
    if total_sum % 10 != 0:
        return "Your card number is invalid."
    
    # Determine the card network
    first_digit = int(card_number[::-1][0])
    first_two_digits = int(card_number[::-1][:2])
    first_three_digits = int(card_number[::-1][:3])
    first_four_digits = int(card_number[::-1][:4])
    
    if first_digit == 4 or first_two_digits == 13 or first_two_digits == 16 or first_two_digits == 19:
        return "Your card is valid.\nYour card network is: Visa"
    elif first_digit == 5 or (first_two_digits >= 2221 and first_two_digits <= 2720):
        return "Your card is valid.\nYour card network is: Mastercard"
    elif first_two_digits == 34 or first_two_digits == 37 or first_two_digits == 4:
        return "Your card is valid.\nYour card network is: American Express"
    elif first_digit == 6 or (first_four_digits >= 622126 and first_four_digits <= 622925):
        return "Your card is valid.\nYour card network is: Discover"
    elif first_two_digits == 62 or first_two_digits == 81 or first_two_digits == 82:
        return "Your card is valid.\nYour card network is: China UnionPay"
    elif first_two_digits == 35 or first_three_digits == 2131 or first_four_digits == 1800:
        return "Your card is valid.\nYour card network is: JCB"
    elif (first_two_digits == 30 or first_two_digits == 36 or first_two_digits == 38 or 
          first_four_digits == 2014 or first_four_digits == 2149):
        return "Your card is valid.\nYour card network is: Diners Club International"
    elif (first_two_digits == 60 or first_three_digits == 608 or first_three_digits == 652 or first_three_digits == 653 
          or first_four_digits == 6071):
        return "Your card is valid.\nYour card network is: RuPay"
    elif first_digit == 6 or first_digit == 5:
        return "Your card is valid.\nYour card network is: Interac"
    elif first_digit == 6 or first_digit == 6014:
        return "Your card is valid.\nYour card network is: EFTPOS"
    elif first_digit == 5 or first_digit == 6 or first_two_digits == 67:
        return "Your card is valid.\nYour card network is: Maestro"
    elif (first_two_digits >= 2205 and first_two_digits <= 2209):
        return "Your card is valid.\nYour card network is: Mir"
    elif (first_digit == 6 or first_digit == 627780 or 
          (first_three_digits >= 636297 and first_three_digits <= 636299)):
        return "Your card is valid.\nYour card network is: Elo"
    elif (first_two_digits == 62 or first_two_digits == 6273 or first_digit == 6014):
        return "Your card is valid.\nYour card network is: NETS"
    elif (first_digit == 4 or (first_four_digits >= 4571 and first_four_digits <= 4599)):
        return "Your card is valid.\nYour card network is: Dankort"
    else:
        return "Your card is valid.\nYour card network is unknown."

while True:
    card_number = input("Enter your credit/debit card number: ")
    if card_number.lower() == "stop":
        break
    result = validate_card(card_number)
    print(result)
