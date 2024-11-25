def add(a,b):
        return a+b
def sub(a,b):
        return a-b
def multi(a,b):
        return a*b
def div(a,b):
        if b==0:
                print("result invalid")
        else:
                return a/b
def mod(a,b):
        return a%b if b!=0 else "modulus by 0 is undefined"

while True:
        print("1.add")
        print("2.sustract")
        print("3.multiply")
        print("4.division")
        print("5.modulus")
        print("6.exit")
        choice=int(input("enter your choice"))
        if choice==6:
                print(f"exiting programme")
                break
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        if choice==1:
                print(f" {a} + {b} = {add(a,b)}")
        elif choice==2:
                print( a,"-",b,"=",sub(a,b))
        elif choice==3:
                print(f" {a} * {b} = {multi(a,b)}")
        elif choice==4:
                print(f" {a} / {b} = {div(a,b)}")
        elif choice==5:
                print(f" {a} % {b} = {mod(a,b)}")
        else:
                print(f"enter invalid choice")
