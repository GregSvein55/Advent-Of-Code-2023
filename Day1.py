# Advent of Code Challenge Day 1 Part 1
# Author: Greg Sveinbjornson
# Date: Dec 1, 2023

def calculate_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r', encoding='cp1047') as file:
        for line in file:
            # Remove leading and trailing whitespaces
            line = line.strip()

            # Find the first and last digits in the line
            first_digit = None
            last_digit = None

            for char in line:
                if char.isnumeric():
                    if first_digit is None:
                        first_digit = int(char)
                    else:
                        last_digit = int(char)
                      

            # Check if last digits are found
            if last_digit is not None:
                # Combine the digits to form a two-digit number
                calibration_value = first_digit * 10 + last_digit
            else:
                # Repeat the digit to form a two-digit number
                calibration_value = first_digit * 10 + first_digit

            # Add the calibration value to the total sum
            total_sum += calibration_value



    return total_sum

# Replace 'aocinput' with the actual path to your input file
file_path = 'aocinput'
result = calculate_calibration_sum(file_path)

print("The sum of all calibration values is:", result)


