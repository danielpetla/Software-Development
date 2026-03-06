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
        start_r = next(tokens) - 1
        start_c = next(tokens) - 1

        # the rest of the input goes to the grid
        grid = [next(tokens) for _ in range(n * n)]
    except StopIteration:
        return
    # Reachability
    reachable = [False] * (n * n)  # the whole grid starts false until proven otherwise
    start_idx = start_r * n + start_c  # initial position in the grid

    # Chechking if initial position is valid
    if 0 <= start_idx < (n * n) and grid[start_idx] < k:
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
                    if not reachable[ni] and grid[ni] < k:
                        reachable[ni] = True
                        queue.append(ni)

    # array to store cells visible at that direction
    v_count = [0] * (n * n)

    # Horizontal
    for y in range(n):

        # west to east
        row_count = 0  # stores clear squares
        for x in range(n):
            idx = y * n + x
            if grid[idx] > k:  # if the light is blocked
                row_count = 0  # reset the counter

            else:  # if the light can pass through
                v_count[idx] += row_count
                row_count += 1

        # east to west
        row_count = 0  # stores clear squares
        for x in range(n - 1, -1, -1):
            idx = y * n + x
            if grid[idx] > k:  # if the light is blocked
                row_count = 0  # reset the counter

            else:  # if the light can pass through
                v_count[idx] += row_count  # record number of squares
                row_count += 1

    # Vertical
    for x in range(n):

        # north to south
        col_count = 0  # stores clear squares
        for y in range(n):
            idx = y * n + x
            if grid[idx] > k:  # if the light is blocked
                col_count = 0  # reset the counter

            else:  # if the light can pass through
                v_count[idx] += col_count
                col_count += 1

        # south to north
        col_count = 0  # stores clear squares
        for y in range(n - 1, -1, -1):
            idx = y * n + x
            if grid[idx] > k:  # if the light is blocked
                col_count = 0  # reset the counter

            else:  # if the light can pass through
                v_count[idx] += col_count
                col_count += 1

    # Find maximum
    max_visi = -1  # if not reachable
    for idx in range(n * n):
        if reachable[idx]:
            # visibility = the cell (1) + counts
            total = 1 + v_count[idx]
            if total > max_visi:
                max_visi = total

    print(max_visi)

# Trigger the function
if __name__ == '__main__':
    solve()
