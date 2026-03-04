# Read inputs
n, m, k = map(int, input().split())
initial_state = tuple(map(int, input().split()))

morphers = []
for _ in range(m):
    data = list(map(int, input().split()))
    fi = data[0]
    ni = data[1]
    # Subtracting 1 to make nests 0-indexed for easier list access
    feeding = [x - 1 for x in data[2:2+fi]]
    nursing = [x - 1 for x in data[2+fi:2+fi+ni]]
    morphers.append((feeding, nursing))

path = []
visited_fails = {}

def dfs(state, depth):
    # CYCLE CHECK: Is the current state >= any ancestor state?
    # If it is, the sequence  can be repeated infinitely.
    for ancestor in path:
        if all(s >= a for s, a in zip(state, ancestor)):
            return True

    # If hit the time limit k, can't search deeper.
    if depth == k:
        return False

    # OPTIMIZATION: If  already failed to find a cycle from this state
    if state in visited_fails and visited_fails[state] <= depth:
        return False

    path.append(state)

    for feeding, nursing in morphers:
        # Check if morph is possible
        possible = True
        for f in feeding:
            if state[f] <= 0:
                possible = False
                break

        if not possible:
            continue

        # Apply morph
        new_state = list(state)
        for f in feeding:
            new_state[f] -= 1
        for nst in nursing:
            new_state[nst] += 1

        # Recursively search the next level
        if dfs(tuple(new_state), depth + 1):
            return True

    # Backtrack
    path.pop()
    visited_fails[state] = depth
    return False


# Start the search
if dfs(initial_state, 0):
    print("Yes")

else:
    print("No")
