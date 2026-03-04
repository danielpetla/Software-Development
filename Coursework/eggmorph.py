# getting the 'bounderies' with the first statement
n, m, k = map(int, input().split())

# second input = first state
initial_state = tuple(map(int, input().split()))

morphers = []  # stores all the morphers

for _ in range(m):
    data = list(map(int, input().split()))
    fi = data[0]  # providing their numbers in the input
    ni = data[1]  # providing their numbers in the input
    feeding = data[2:2+fi]
    nursing = data[2+fi:2+fi+ni]
    morphers.append((feeding, nursing))

# queue stores (state, depth) -> depth is counting the total tries
queue = [(initial_state, 0)]
seen = {initial_state}

front = 0  # index of next element to process

# process every possible state
while front < len(queue):
    state, depth = queue[front]
    front += 1

    # meas we are not allowed to apply more morphs
    if depth == k:
        continue

    # try every morpher in the current state
    for feeding, nursing in morphers:
        new_state = list(state)  # current state is a tuple, new state isn't

        # check if morph is possible
        possible = True
        for f in feeding:
            if new_state[f-1] <= 0:
                possible = False
                break

        if not possible:
            continue

        # apply morph
        for f in feeding:
            new_state[f-1] -= 1
        for nst in nursing:
            new_state[nst-1] += 1

        new_state = tuple(new_state)  # conversting back to tuple

        if new_state in seen:
            print("Yes")
            exit()

        seen.add(new_state)
        queue.append((new_state, depth + 1))

print("No")
