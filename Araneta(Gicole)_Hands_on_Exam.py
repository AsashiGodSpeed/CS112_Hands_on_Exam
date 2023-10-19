Choose = int(input(" [1] - Decimal to Binary \n [2] - Decimal to Octal \n [3] - Decimal to Hexadecimal "
                   "\nEnter a Number based on the conversion: "))

if Choose == 1:
    Decimal = int(input("Enter a Decimal Number: "))
    Bi = format(Decimal, "b")
    print(Bi)
elif Choose == 2:
    Decimal = int(input("Enter a Decimal Number: "))
    Oct = format(Decimal, "o")
    print(Oct)
elif Choose == 3:
    Decimal = int(input("Enter a Decimal Number: "))
    Hex = format(Decimal, "x")
    print(Hex)
else:
    print("Invalid input. Please try again.")
