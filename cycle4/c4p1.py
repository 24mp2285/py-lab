def fibonacci(i):
        if i<=1:
                return i
        else:
                return fibonacci(i-1)+ fibonacci(i-2)
number=int(input("enter the number of terms:"))
if number<=0:
        print("enter a positive number")
else:
        print("fibonacci sequence:")
        for i in range(number):
                print(fibonacci(i),end=" ")
