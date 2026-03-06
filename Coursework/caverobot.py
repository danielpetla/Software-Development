from collections import deque
import sys
import string

def solve_maze():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines: return -1

    if lines[0][0].isdigit():
            grid = lines[1:]
    else:
        grid = lines

    rows, cols = len(grid), len(grid[0])  # w and h

    start = end = None
    total_plates = {}

    # Initial scan
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char == 'S': start = (r, c)  # location of the start
            if char == 'E': end = (r, c)  # location of the end
            elif char.islower():  # = pressure plate
                total_plates[char] = total_plates.get(char, 0) + 1

    # safety check:
    if start is None or end is None:
        return - 1 # exit is unrechable

    # state track
    plates_found = {k: 0 for k in total_plates}
    door_open = {}
    unsure_doors = {}

    # preconfigure doors
    for k in string.ascii_uppercase:
        door_open[k] = (k.lower() not in total_plates)
        unsure_doors[k] = []

    # inialize search
    visited = set([start])
    queue = deque([(start[0], start[1], 0)])  # stores: row, col, distance

    # The search
    while queue:
        r, c, dist = queue.popleft()

        if (r,c) == end:
            return dist  # exit found

        # orthogonal exploring
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0,1)]:
            nr, nc = r + dr, c + dc

            # bounderys and visited
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                char = grid[nr][nc]

                if char == "#":  # wall
                    continue

                if char.isupper() and char not in ['S', 'E']:  # it is a door
                    if not door_open[char]:
                        # door is locked: save position and follow other path
                        unsure_doors[char].append((nr, nc, dist + 1))
                        continue

                # cell is walkable
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

                if char.islower():  # plate
                    plates_found[char] += 1

                    # find if it is the last plate of the type
                    if plates_found[char] == total_plates[char]:
                        door_char = char.upper()
                        door_open[door_char] = True  # unlock door

                        # all doors in waiting
                        for pr, pc, pdist in unsure_doors[door_char]:
                            if (pr, pc) not in visited:
                                visited.add((pr, pc))
                                queue.append((pr, pc, pdist))

                        # clear pending of this door type
                        unsure_doors[door_char] = []

    # exit not reachable
    return -1


# Trigger the function
if __name__ == '__main__':
    print(solve_maze())
