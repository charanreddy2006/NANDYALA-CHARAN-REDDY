
#Task 1:
n=int(input("Enter your number: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

result = factorial(n)
print(f"factorial of {n} is {result}")

#Task 2:
n=float(input("Enter your number: "))
import math
if n>0:
    print("square root: math.sqrt(n)")
else:
    print("Enter a number greater than 0")

if n>0:
    print('logarithm: math.log(n)')
else:
    print("Enter a number greater than 0")

print('sine: math.sin(n)')