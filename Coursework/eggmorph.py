# first input
numbers = list(map(int, input().split()))
mnk = {'n': numbers[0], 'm': numbers[1], 'k': numbers[2]}

# initial state
state = list(map(int, input().split()))

states = []   # store all states

# applying morph
for r in range(mnk['k']):

    w_input = list(map(int, input().split()))

    fi = w_input[0]
    ni = w_input[1]

    feeding_nests = w_input[2:2+fi]
    nursing_nests = w_input[2+fi:2+fi+ni]

    # subtract 1 egg
    for nest in feeding_nests:
        state[nest-1] -= 1

    # add 1 egg
    for nest in nursing_nests:
        state[nest-1] += 1

    states.append(state.copy())

# check repetition
seen = []

for st in states:
    if st in seen:
        print("Yes")
        break

    seen.append(st)
else:
    print("No")
