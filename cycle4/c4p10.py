nums=list(map(int,input("enter number").split()))
multiples_of_three = list(filter(lambda x: x % 3 == 0, nums))
print("Multiples of 3:", multiples_of_three)
