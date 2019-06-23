print("Program define if the Entered numbers even or odd ")
print('\n')
print("And divide them \" the first divided by the second number\"")
print('\n')

num1 = int(input("Enter first integer number:"))
num2 = int(input("Enter second integer number:"))

if num1 % 2 == 0:
    print("You First number is EVEN")
else:
    print("You First Number is ODD")

print('\n')

if num2 % 2 == 0:
    print("You Second number is EVEN")
else:
    print("You Second Number is ODD")

print('\n')


def divide(n1, n2):
    try:
        result = n1 / n2
        print(n1, " divided by ", n2, "=", result)
    except ZeroDivisionError:
        print("You Cannot divide by 0.")
    except:
        print("Please Enter an Integer number")


divide(num1, num2)
