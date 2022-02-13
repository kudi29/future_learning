while True:

    try:

        funds = float(input("Enter amount to transfer: "))

        if funds < 0:

            raise Exception("Please enter a positive value,")

        break

    except ValueError:

        print("Please enter a numeric value,")
