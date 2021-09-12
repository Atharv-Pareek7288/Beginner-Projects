#Faulty calculator


security1 = 72698582

print("Enter your first number: ")
num1 = int(input())

print("Enter your second number: ")
num2 = int(input())

print("Enter Which operation you want: +, -, *, / ")
num3 = input()

print("If you want answer to question, first type security key. To type security key enter (y) else (n)")
num4 = input()

if num4 == "y":
    print("security key")
    security = int(input())
    if security == security1:
        if num3 == "*":
            multiply = num1*num2
            print(multiply)

        elif num3 == "+":
            addition = num1+num2
            print(addition)

        elif num3 == "-":
            substraction = num1-num2
            print(substraction)

        elif num3 == "/":
            Divide = num1/num2
            print(Divide)

# These are the faulty answers for few questions

    else:
        if num1 == 45 and num2 == 3 and num3 == "*":
            print("Your answer is: 555")

        elif num1 == 56 and num2 == 9 and num3 == "+":
            print("Your answer is: 77")

        elif num1 == 56 and num2 == 6 and num3 == "/":
            print("Your answer is: 4")

    


else:
    print("Ok, Thank you for using me")    


               
               
               
           
























