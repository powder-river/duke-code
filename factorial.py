def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

user_input = int(input("Enter a number to find it's factorial:\n"))
print("The factorial of {} is {}".format(user_input,factorial(user_input)))
