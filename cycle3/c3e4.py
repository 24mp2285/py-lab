def perfectSquares(l, r):
    for i in range(l, r + 1):
        if i >= 0: 
            sqrt_i = int(i ** 0.5)
            if sqrt_i * sqrt_i == i and i % 2 == 0:
                print(i, end=" ")

while True:
    try:
        l = int(input("Enter the lower range: "))
        r = int(input("Enter the upper range: "))
        if l > r:
            print("The lower range must be less than or equal to the upper range.")
            continue
        break
    except ValueError:
        print("Please enter valid integers.")

perfectSquares(l, r)
