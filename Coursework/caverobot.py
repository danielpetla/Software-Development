from collections import deque
import sys
import string

def solve():
    lines = [line for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines: return

    first_line = lines[0].split()
    w = int(first_line[0])  # columns
    h = int(first_line[1])  # rows

    grid = lines[1:1 + h]

    total_plates = {}
    wormholes = {str(i): [] for i in range(1, 10)}
    start = None

    # pre-scan
    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if 'a' <= char <= 'z':
                total_plates[char] = total_plates.get(char, 0) + 1
            elif '1' <= char <= '9':
                wormholes[char].append((r, c))
            elif char == '=':
                start = (r, c)

    if not start:
        print("No")
        return

    # state initialize
    initial_pressed = frozenset()
    visited = set([(start[0], start[1], initial_pressed)])

    # tracks: row, col, pressed plates, distance
    q = deque([(start[0], start[1], initial_pressed, 0)])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Search
    while q:
        r, c, pressed, dist = q.popleft()
        char = grid[r][c]

        # exit found
        if char == '!':
            print("Yes")
            return

        # wormhole
        if '1' <= char <= '9':
            for wr, wc in wormholes[char]:
                # if wormhole not visited -> exit
                if (wr, wc, pressed) not in visited:
                    visited.add((wr, wc, pressed))
                    # moving
                    q.appendleft((wr, wc, pressed, dist))

        # orthogonal moviment
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < h and 0 <= nc < w:
                nchar = grid[nr][nc]

                if nchar == '#':
                    continue

                # doors
                if 'A' <= nchar <= 'Z':
                    req_plate = nchar.lower()
                    if req_plate in total_plates:
                        # count plates pressed
                        pressed_count = sum(1 for pr, pc in pressed if grid[pr][pc] == req_plate)
                        if pressed_count < total_plates[req_plate]:
                            continue  # not possible

                # plates
                new_pressed = pressed
                if 'a' <= nchar <= 'z' and (nr, nc) not in pressed:
                    new_pressed = pressed | frozenset([(nr, nc)])

                # check visited
                if (nr, nc, new_pressed) not in visited:
                    visited.add((nr, nc, new_pressed))
                    q.append((nr, nc, new_pressed, dist + 1))

    # not possible
    print("No")

# Trigger function
if __name__ == '__main__':
    solve()
