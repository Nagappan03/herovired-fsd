def console():
    print("Welcome to our calculator application!")
    print("--------------------------------------")
    print("1. Factorial")
    print("2. Palindrome")
    print("3. Fibonacci")
    print("4. Table of a given number")
    print("5. Exit")
    option = int(input("Please select any one of the above options to proceed: "))
    calculator(option)

def factorial(num):   
    factorial = 1    
    if num < 0 or num == 0:    
        print("Please enter a number greater than 0")
        print()    
    elif num == 1:    
        print("The factorial of 1 is 1 itself")
        print()    
    else:
        temp = num
        while(num > 1):
            factorial = factorial * num
            num = num - 1
        print("Factorial of",temp,"is",factorial)
        print()

def palindrome_num(num):
    temp = num
    reverse = 0
    while(num > 0):
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if(temp == reverse):
        print("The number is a palindrome!")
        print()
    else:
        print("The number isn't a palindrome!")
        print()

def palindrome_str(str):
    str = str.casefold()
    reverse = reversed(str)
    str_list = list(str)
    reverse_list = list(reverse)
    if (str_list == reverse_list):
        print("The string is a palindrome")
        print()
    else:
        print("The string is not a palindrome")
        print()

def fibonacci(num):
    n1 = 0
    n2 = 1
    count = 0
    series = []
    if (num <= 0):
        print("Please enter a number greater than 0")
        print()
    elif (num == 1):
        print("The Fibonacci series of the numbers upto",num,"is: ",num)
        print()
    else:
        print("The Fibonacci series of the numbers upto",num,"is: ")
        while (count < num):
            series.append(n1)
            sum = n1 + n2
            n1 = n2
            n2 = sum
            count = count + 1
        print(series)
        print()

def tables(num, lastValue):
    print("The Multiplication Table of",num,"upto",lastValue,"is: ")    
    for i in range(1, lastValue + 1):      
        print(num, '*', i, '=', num * i)
    print()

def calculator(option):
    if(option == 1):
        num = int(input("Please enter a number to find the factorial of it: "))
        factorial(num)
    elif(option == 2):
        val = int(input("Please enter 1 to find the palindrome for a number or 2 to find the palindrome for a string: "))
        if(val == 1):
            opt = int(input("Now please enter a number to proceed: "))
            palindrome_num(opt)
        elif(val == 2):
            opt = input("Now please enter a string to proceed: ")
            if(opt.isalpha() == False):
                print("Please enter an alphabetical word")
                print()
            else:
                palindrome_str(opt)
        else:
            print("Please enter either 1 or 2")
            print()
    elif(option == 3):
        num = int(input("Please enter a number to find the fibonacci series of it: "))
        fibonacci(num)
    elif(option == 4):
        num = int(input("Please enter a number of which you want to print the multiplication tables: "))
        range = int(input("Please enter the range upto which you want to print the multiplication tables: "))
        tables(num, range)
    elif(option == 5):
        print("Thank you.!")
        exit()
    else:
        print("Please select any options from 1 to 5: ")
        print()
    console()

console()