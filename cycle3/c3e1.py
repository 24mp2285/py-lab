num=int(input("enter the number"))
fact=1
if num<0:
        print("enter a valid number")
elif num==0:
        print("the factorial of 0 is 0")
else:
        for i in range(1,num+1):
                fact=fact*i
print(f"the factorial of {num} is {fact}")
