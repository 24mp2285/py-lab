total=0
list1=[int(num)for num in input("enter  the numbers in the list:").split()]
for ele in range(0,len(list1)):
        total=total+list1[ele]
print("sum of all elements in given list:",total)
