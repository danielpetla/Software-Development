import collections
import sys

def solve():
    # reading the whole input and splitting it
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # iterator to get the numbers one by one
    tokens = iter(map(int, input_data))

    try:
        # read the first line
        n = next(tokens)
        k = next(tokens)

        # adjust 1 based coordinates into 0 based
        start_c = next(tokens) - 1
        start_r = next(tokens) - 1

        # the rest of the input goes to the grid
        grid = [next(tokens) for _ in range(n * n)]
    except StopIteration:
        return

    # Reachability
    reachable = [False] * (n * n)  # the whole grid starts false until proven otherwise
    start_idx = start_r * n + start_c  # initial position in the grid

    # Chechking if initial position is valid
    if 0 <= start_r < n and 0 <= start_c < n:
        start_idx = start_r * n + start_c

   # Checking if the position is reachable
    if 0 <= start_idx < (n * n) and grid[start_idx] <= k:
        queue = collections.deque([start_idx])  # starting point inserted in the queue
        reachable[start_idx] = True  # marking the starting point as true

        # exploration loop
        while queue:
            curr = queue.popleft()
            r, c = divmod(curr, n)  # turning the index back to (x, y)

            # checking neighbor directions (up, down, left, right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    ni = nr * n + nc
                    if not reachable[ni] and grid[ni] <= k:
                        reachable[ni] = True
                        queue.append(ni)

    # array of zeros to store the vision count for each cell
    v_count = [0] * (n * n)

# Horizontal processing
    for r in range(n):
        row_start = r * n

        # Left (west)
        L = [-1] * n  # stores the index of the nearest taller mountain to the left
        stack = []
        for c in range(n):
            idx = row_start + c
            val = grid[idx]
            while stack and grid[row_start + stack[-1]] <= val:
                stack.pop()
            if stack:
                L[c] = stack[-1]
            stack.append(c)  # add the current mountain's index to the stack for future cells

        # Right (east)
        # iterate backwards to find blockers on the right
        R = [n] * n  # stores the index of the nearest taller mountain to the right
        stack = []
        for c in range(n - 1, -1, -1):
            idx = row_start + c
            val = grid[idx]
            while stack and grid[row_start + stack[-1]] <= val:
                stack.pop()
            if stack:
                R[c] = stack[-1]
            stack.append(c)  # add the current mountain's index to the stack for future cells

        # Adding horizontal visible cells
        for c in range(n):
            idx = row_start + c
            v_count[idx] += (c - L[c] - 1) + (R[c] - c - 1)

    # Vertical
    for c in range(n):

        # Up (north)
        L = [-1] * n  # stores the index of the nearest taller mountain to the up
        stack = []
        for r in range(n):
            idx = r * n + c
            val = grid[idx]
            while stack and grid[stack[-1] * n + c] <= val:
                stack.pop()
            if stack:
                L[r] = stack[-1]
            stack.append(r)  # add the current mountain's index to the stack for future cells

        # Down (south)
        # iterate backwards to find blockers down
        R = [n] * n  # stores the index of the nearest taller mountain to the down
        stack = []
        for r in range(n - 1, -1, -1):
            idx = r * n + c
            val = grid[idx]
            while stack and grid[stack[-1] * n + c] <= val:
                stack.pop()
            if stack:
                R[r] = stack[-1]
            stack.append(r)  # add the current mountain's index to the stack for future cells

        # Adding vertical visibel cells
        for r in range(n):
            idx = r * n + c
            v_count[idx] += (r - L[r] - 1) + (R[r] - r - 1)

    # impossible case
    max_visi = -1

    for idx in range(n * n):
        if reachable[idx]:
            total = 1 + v_count[idx]
            if total > max_visi:
                max_visi = total

    print(max_visi)

# Trigger the function
if __name__ == '__main__':
    solve()
