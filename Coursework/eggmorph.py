# getting the number of n, n and k
spec_input = input()
numbers_str = spec_input.split()
numbers = [int(num) for num in numbers_str]  # splitting the numbers of the input

mnk = {'n': numbers[0], 'm': numbers[1], k: numbers[2]}  # connecting the values to the right keys

# getting the input os the morphs
nest_input = input()
unfold = nest_input.split()
fi_ni = {'fi': unfold[0], 'ni': unfold[1]}
