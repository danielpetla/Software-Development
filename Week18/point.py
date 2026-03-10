class Point:
    def __init__(self, x, y, z):
        # Change this to store x y and z in self

    def __str__(self):
        # Change this to format the point nicely
        return "POINT"

    def __eq__(self, o):
        if self is o:
            return True
        if not instanceof(o, Point):
            return False
        # Change this to properly compare two points
        return True

    def __hash__(self):
        # Change this to compute a proper hash. Use hash(...)
        return 0



def main():
    l = [Point(1,2,3), Point(0,0,0), Point(3, 2, 1), Point(1, 2, 3)]
    print("List:")
    for p in l:
        print(p)
    print()
    print("Set:")
    for p in set(l):
        print(p)
    print()
    print(f"Equality: {Point(1, 2, 3) == Point(1, 2, 3)}")
    

if __name__ == "__main__":
    main()
