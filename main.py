# Recursion Is Simply Function Inside same function

# This Is The Example Of Iterative Function To Find Factorial Of A Number passed to it
print("Press 1 To use Iterative Function To Find Factorial\n"
      "Press 2 To Use Recursive Function To Find Factorial\n"
      "Your Choice: ",end="")
choice = int(input())


if(choice == 1):
    print("Iterative Factorial Function is Running\n")
    def factorial_iterative(n):
        """
        :param n:  Integer
        :return:  n * n-1 * n-2 * n-3 * ..... * 1
        """

        factorial = 1
        for i in range(n):
            factorial = factorial * (i+1)
        return factorial

    bool = 1

    while(bool == 1):
        print("Enter Number To Find Its Factorial/Enter 0 To Exit The Program: ",end="")
        number = int(input())

        if(number == 0):
            bool = 0

        print(factorial_iterative(number))
elif(choice == 2):
    # This Is The Example Of Recursive Function To Find Factorial Of A Number passed to it
    print("Recursive Factorial Function is Running\n")

    def factorial_recursion(n):
        """
        :param n:  Integer
        :return:  n * n-1 * n-2 * n-3 * ..... * 1
        """

        if n == 1:
            return 1
        else:
            return n * factorial_recursion(n-1)

    bool = 1

    while(bool == 1):
        print("Enter Number To Find Its Factorial/Enter 0 To Exit The Program: ",end="")
        number = int(input())

        if(number == 0):
            bool = 0

        print(factorial_recursion(number))

else:
    print("Enter A Valid Choice")


# How recursive factorial function works

# Let say you entered 5

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = n which is returned