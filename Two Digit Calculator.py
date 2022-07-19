calcloop = "yes"
while calcloop == 'yes':

    print("Two number calculator")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    numin = input("Select:")

    if numin in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if numin == '1':
            numout = num1 + num2
        elif numin == '2':
            numout = num1 - num2
        elif numin == '3':
            numout = num1 * num2
        elif numin == '4':
            numout = num1 / num2
        print(round(numout,2));
        calcloop = input("Do you want to restart? \nyes or no?")

        if calcloop == 'no':
            print("Cya")

