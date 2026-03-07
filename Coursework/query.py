import sys

def build(parsed, index):
    depth, text = parsed[index]
    op = text.split()[0]

    # boolean operations with children
    if op in ["AND", "OR"]:
        children = []
        next_idx = index + 1
        if next_idx < len(parsed):
            c_depth = parsed[next_idx][0]
            # this children share the same indentation
            if c_depth > depth:
                while next_idx < len(parsed) and parsed[next_idx][0] == c_depth:
                    c_node, next_idx = build(parsed, next_idx)
                    children.append(c_node)
        return (op, children), next_idx

    elif op == "NOT":
        next_idx = index + 1
        c_node, next_idx = build(parsed, next_idx)
        return (op, [c_node]), next_idx

    # leaf queries
    else:
        rem = text[len(op):].strip()
        prop = rem.split()[0]
        rem2 = rem[len(prop):].strip()

        if op in ["CONTAINS", "EQUALS", "STARTSWITH", "ENDSWITH"]:
            # strip the quotes
            val = rem2[1: -1]
            return (op, prop, val), index + 1

        else:
            # parse (float or int)
            val = float(rem2) if 'F' in op else int(rem2)
            return(op, prop, val), index + 1

def evaluate(node, entry):
    op = node[0]

    if op == "AND":
        return all(evaluate(child, entry) for child in node[1])
    elif op == "OR":
        return any(evaluate(child, entry) for child in node[1])
    elif op == "NOT":
        return not evaluate(node[1][0], entry)
    else:
        prop = node[1]
        val = node[2]
        entry_val = entry[prop]

        if op == "LESSTHAN" or op == "FLESSTHAN":
            return entry_val < val
        elif op == "GREATERTHAN" or op == "FGREATERTHAN":
            return entry_val > val
        elif op == "CONTAINS":
            return val in entry_val
        elif op == "EQUALS":
            return entry_val == val
        elif op == "STARTSWITH":
            return entry_val.startswith(val)
        elif op == "ENDSWITH":
            return entry_val.endswith(val)

def solve():
    # read input
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n, m, k = map(int, lines[0].split())
    prop_names = lines[1].split(',')
    prop_types = lines[2].split(',')

    data = []
    # dict list
    for i in range (n):
        vals = lines[3+i].split(',')
        entry = {}
        for j in range(m):
            t = prop_types[j]
            if t.startswith('int'):
                entry[prop_names[j]] = int(vals[j])
            elif t == 'float':
                entry[prop_names[j]] = float(vals[j])
            else:
                entry[prop_names[j]] = vals[j]
        data.append(entry)

    query_l = lines[3 + n : 3 + n + k]

    parsed = []
    # identify depth
    for line in query_l:
        stripped = line.lstrip(' \t')
        if not stripped:
            continue
        depth = len(line) - len(stripped)
        parsed.append((depth, stripped))

    if parsed:
        tree, _ = build(parsed, 0)
        # Evaluate how many queries hit True against the parsed Abstract Syntax Tree
        ans = sum(1 for entry in data if evaluate(tree, entry))
        print(ans)
    else:
        print(n)

if __name__ == '__main__':
    sys.setrecursionlimit(2500)
    solve()
