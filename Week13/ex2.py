l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (l1)

# -----------------------------------------------

a = range(11)
l2 = list(a)
print(l2[1:])

# ------------------------------------------------

n = list(l2)
result = []  # I need to store what I'm generating
for i in n:
    # Here I'm storing 'number' + each element of the list n in the empty list result
    result.append(f"Number: {i}")
print(result)

# ------------------------------------------------

l3 = list(range(11))
evens = l3[::2]
print(evens)

# ------------------------------------------------

even = result[2:11:2]
print(";".join(even))
