#Collatz Conjecture - Start with a number n > 1.
#Find the number of steps it takes to reach
#one using the following process: If n is even,
#divide it by 2. If n is odd, multiply it by 3 and add 1.


n = input("Enter a number - ")

try:
    n = int(n)
    if n < 1:
        print("Number is too small")
    elif n > 1:
        if n % 2 == 0:
            n = n/2
            print(n)
        elif n % 2 !=0:
            n = n * 3 + 1
            print(n)
except:
    print("Enter a valid number")
