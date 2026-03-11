import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, o):
        if self is o:
            return True
        if not isinstance(o, Point):
            return False
        if self.x == o.x and self.y == o.y and self.z == o.z:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    # --- New Methods ---

    def largest(self):
        """Returns the largest component of the point."""
        return max(self.x, self.y, self.z)

    def norm(self):
        """Computes the Euclidean norm of the point."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross_product(self, q):
        """Computes the cross product of this point and another point q."""
        cx = self.y * q.z - self.z * q.y
        cy = self.z * q.x - self.x * q.z
        cz = self.x * q.y - self.y * q.x
        return Point(cx, cy, cz)

    # --- Magic Methods ---

    def __abs__(self):
        """Absolute value returns the norm of the point."""
        return self.norm()

    def __add__(self, o):
        """Adding two points creates a summed point."""
        if isinstance(o, Point):
            return Point(self.x + o.x, self.y + o.y, self.z + o.z)
        return NotImplemented

    def __mul__(self, scalar):
        """Multiplying with a number returns the scaled point."""
        if isinstance(scalar, (int, float)):
            return Point(self.x * scalar, self.y * scalar, self.z * scalar)
        return NotImplemented


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
    print()

    # Testing the new methods
    print("--- Testing New Methods ---")
    p1 = Point(-10, 2, 8)
    print(f"Largest of {p1}: {p1.largest()}")

    p2 = Point(1, 1, 1)
    print(f"Norm of {p2}: {p2.norm()}")

    p3 = Point(1, 0, 0)
    p4 = Point(0, 1, 0)
    print(f"Cross Product of {p3} and {p4}: {p3.cross_product(p4)}")

    print(f"Absolute value (__abs__) of {p2}: {abs(p2)}")
    print(f"Addition (__add__) of {p3} and {p4}: {p3 + p4}")
    print(f"Scalar Multiplication (__mul__) of {p2} * 5: {p2 * 5}")

if __name__ == "__main__":
    main()
