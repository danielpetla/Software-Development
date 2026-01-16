n = int(input("Please enter a number n: "))
while n != 1:
    if n % 2 == 0:
        n = n / 2
        print(f"{n*2} -> {n}")
    else:
        n = (3*n) + 1
        print(f"{(n-1) // 3} -> {n}")

print("\n")