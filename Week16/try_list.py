SIZE = 10

def read_numbers():
    numbers = []
    count = 0
    for _ in range(SIZE):
        try:
            numbers.append(int(input()))
        except ValueError:
            print("The number should be a intager")
            count += 1
            if count == 3:
                print("You made the same mistake 3 times")
            if count == 5:
                print("No more chances, you nerver learn")
                quit()
    return numbers


l = read_numbers()
print(" ".join(str(i) for i in l))
