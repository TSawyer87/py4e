#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.

total = 0
count = 0

while True:
    # Get user input
    user_input = input("Enter a number:(or 'done' to finish): ")

    # Check if user wants to quit
    if user_input.lower() == 'done':
        break

    # Try converting input to a number
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter a number.")

    # Calculate average (avoid division by zero)
    if count > 0:
        average = total / count
        print(f"Total: {total:.2f}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
    else:
        print("No numbers were entered.")



