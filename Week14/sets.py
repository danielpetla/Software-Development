# Part 1
l1 = [1, 2, 1, 3, 1, 4]
s1 = {1, 2, 1, 3, 1, 4}
s2 = set(range(11))

print("Set 2 = ", s2)
print("List = ", l1)
print("Set 1 = ", s1)

# ------------------------------------------------

# Part 2

strin = input("Please insert a string: ")
l3 = strin.split()
s3 = set(l3)

st3 = enumerate(s3)
se3 = list(st3)

print("Set 3 =", s3)
print("Set 3 enumerated =", se3)
