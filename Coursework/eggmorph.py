# getting the number of n, n and k
spec_input = input()
numbers_str = spec_input.split()
numbers = [int(num) for num in numbers_str]  # splitting the numbers of the input

mnk = {'n': numbers[0], 'm': numbers[1], 'k': numbers[2]}  # connecting the values to the right keys

state_input = input()
spl_str = state_input.split()
state = [int(s) for s in spl_str]  # splitting the numbers of the input


# getting the input os the morphs
nest_input = input()
unfold = nest_input.split()
w_input = [int(m) for m in unfold]
feeding_nests = w_input[2:2+fi]
nursing_nests = w_input[2+fi:2+fi+ni]

# subtract 1 egg from them
for nest in feeding_nests:
    state[nest-1] -= 1  # -1 because nests are 1-indexed in input

for nest in nursing_nests:
    state[nest-1] += 1  # -1 because nests are 1-indexed in input
