print("Number System Counter")

while True:
    try:
        start = int(input("Enter starting number: "))
        amount = int(input("Enter how many numbers to display: "))
        break

    except ValueError:
        print("Please enter an integer value.\n")


for number in range(start, start + amount):
    # Convert to hexadecimal
    hex_number = hex(number)[2:].upper()
    # Convert to binary
    binary_number = bin(number)[2:]

    print(f"DECIMAL:{number}  HEXADECIMAL:{hex_number}  BINARY:{binary_number}")

