#Task_01

a=int(input('Enter a number: '))
if (a % 2 == 0):
    print(f'{a} is an even number')
else:
    print(f'{a} is an odd number')

#Task_02
sum = 0
for i in range(1,51):
    sum = sum + i
print("the sum of numbers from 1 to 50 is:",sum)