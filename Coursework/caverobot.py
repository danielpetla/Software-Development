import sys
from collections import deque

def solve():
    # read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    w = int(input_data[0])  # columns
    h = int(input_data[1])  # rows
    grid = input_data[2:]

    start = None
    total_plates = {}
    wormholes = {}

    # parse grid
    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if char == '=':
                start = (r, c)
            elif char.islower():
                total_plates[char] = total_plates.get(char, 0) + 1
            elif char.isdigit():
                if char not in wormholes:
                    wormholes[char] = []
                wormholes[char].append((r, c))

    # state trackers
    visited = set()
    pressed_plates = set()
    pressed_counts = {}
    opened_doors = set()

    # doors encountered
    blocked_doors = {}
    used_wormholes = set()

    q = deque()
    q.append(start)
    visited.add(start)

    while q:
        r, c = q.popleft()
        char = grid[r][c]

        # exit reached
        if char == '!':
            print("Yes")
            return

        # plates
        if char.islower():
            if (r, c) not in pressed_plates:
                pressed_plates.add((r, c))
                pressed_counts[char] = pressed_counts.get(char, 0) + 1

                # checking if required plates wore pressed
                if pressed_counts[char] == total_plates[char]:
                    door_char = char.upper()
                    opened_doors.add(door_char)

                    # blocked doors and keep exploring
                    if door_char in blocked_doors:
                        for dr, dc in blocked_doors[door_char]:
                            if (dr, dc) not in visited:
                                visited.add((dr, dc))
                                q.append((dr, dc))
                        del blocked_doors[door_char]

        # wormhole
        if char.isdigit():
            if char not in used_wormholes:
                used_wormholes.add(char)
                # adds all wormholes
                for wr, wc in wormholes[char]:
                    if (wr, wc) not in visited:
                        visited.add((wr, wc))
                        q.append((wr, wc))

        # orthogonal moviment
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < h and 0 <= nc < w:
                nchar = grid[nr][nc]

                if nchar == '#':
                    continue

                if nchar.isupper():
                    if nchar in opened_doors:
                        # open door -> walk trough
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                    else:
                        # locked door -> remember location
                        if nchar not in blocked_doors:
                            blocked_doors[nchar] = set()
                        blocked_doors[nchar].add((nr, nc))
                else:
                    # empty space, exit of wormhole
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

    # oterwise
    print("No")

# Trigger the function
if __name__ == '__main__':
    solve()
