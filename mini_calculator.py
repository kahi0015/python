def calculate_sum_and_difference():
    # Initialize variables for sum and difference
    sum_of_numbers = 0
    difference_of_numbers = None

    # Prompt the user for input and continue until 'q' is entered
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        # Check if the input is 'q' to quit the loop
        if user_input == 'q':
            break

        try:
            number = float(user_input)  # Convert the input to a float
            sum_of_numbers += number  # Add the number to the sum

            if difference_of_numbers is None:
                difference_of_numbers = number
            else:
                difference_of_numbers -= number  # Subtract the number from the difference
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q'.")

    # Print the sum and difference
    print("Sum of the numbers:", sum_of_numbers)
    print("Difference of the numbers:", difference_of_numbers)


calculate_sum_and_difference()