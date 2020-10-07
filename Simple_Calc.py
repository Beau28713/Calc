#Simple calc.
#Here is my simple calc that can do multiplication, division, addition,
#subtraction, and power of.
#Just enter a number, then press enter, enter the calculation type and press
#enter again, finally enter the second number and press enter one last time. 

choice = True

while choice:
    
    num1 = input("Enter first number: ")
    calculation = input("Enter type of calculation: ")
    num2 = input("Enter second number: ")

    if calculation == "*":
        answer = int(num1) * int(num2)
        print(str(num1) + " * " + str(num2) + " = " + str(answer))

    if calculation == "/":
        answer = int(num1) / int(num2)
        print(str(num1) + " / " + str(num2) + " = " + str(answer))

    if calculation == "+":
        answer = int(num1) + int(num2)
        print(str(num1) + " + " + str(num2) + " = " + str(answer))

    if calculation == "-":
        answer = int(num1) - int(num2)
        print(str(num1) + " - " + str(num2) + " = " + str(answer))

    if calculation == "^":
        answer = pow(int(num1), int(num2))
        print(str(num1) + " ^ " + str(num2) + " = " + str(answer))

    usercontinue = input("Would like to do another calculation. Yes or No: ")

    if usercontinue.lower() == "no":
        choice = False


