print("\nWelcome to my basic computer calculator\n".title())

choice = 0

new_line = "\n"

while choice != 5:

    print("Enter 1 for Addition".title())
    print("Enter 2 Subtraction".title())
    print("Enter 3 Multiplication".title())
    print("Enter 4 Division".title())
    print("Enter 5 Exit".title())

    choice = int(input("\nEnter choice between 1 to 5: "))

    if choice in range(1, 5):

        first_number = float(input("Enter first number: "))

        second_number = float(input("Enter Second number: "))

        if choice == 1:

            try:

                result = first_number + second_number
                print(f'{new_line} Result: {result} {new_line}')

            except (ValueError, RuntimeError, TypeError, NameError):

                print("Please enter a number")

        elif choice == 2:

            result = first_number - second_number

            print(f'{new_line} Result: {result} {new_line}')

        elif choice == 3:

            result = first_number * second_number

            print(f'{new_line} Result: {result} {new_line}')
        elif choice == 4:

            try:

                result = first_number / second_number

                print(f'{new_line} Result: {result} {new_line}')

            except (ZeroDivisionError, ValueError, RuntimeError, TypeError, NameError):

                print("\ncan't divide by 0\n")

    elif choice == 5:

        break

    else:
        print("Invalid choice!! Please retry")

print("Thanks for using my bisic computer calculator".title())
