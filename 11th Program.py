#Python Program to Print all Prime Numbers in an Interval

lower = int(input("Enter The NUmber : "))
upper = int(input("Enter The NUmber : "))

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)