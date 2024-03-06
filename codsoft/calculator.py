print ("Menu of operation\nEnter the character\n1. Addition(A)\n2. Subtraction(S)\n3. Multiplication(M)\n4. Division(D)\n5. Modulus(R)\n6. Exit(E)")

while True: 
    operation = input("What operation would you like to perform: ").upper()

    if operation == 'E':
        print ("Exiting program")
        break
    if operation in ['A', 'S', 'M', 'D', 'R']:
        num1 = float(input("Enter thr first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "A":
            result = num1 + num2
        elif operation == "S":
            result = num1 - num2
        elif operation == "M":
            result = num1 * num2
        elif operation == "D":
            result = num1 / num2
        elif operation == "R":
            result = num1 % num2
        print ("Result: ", result)
    else:
        print("Invalid input, try again")

    


