from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, pts):
        if len(pts) != 2:
            raise ValueError("Expected two points")
        p1, p2 = pts
        return cls(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def top(self):
        return self.pt2.y

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point(
            (self.pt1.x + self.pt2.x) / 2,
            (self.pt1.y + self.pt2.y) / 2
        )

    def area(self):
        return self.width * self.height

    def move(self, x, y):
        return Rectangle(
            self.pt1.x + x,
            self.pt1.y + y,
            self.pt2.x + x,
            self.pt2.y + y,
        )

    def intersection(self, other):
        x1 = max(self.left, other.left)
        y1 = max(self.bottom, other.bottom)
        x2 = min(self.right, other.right)
        y2 = min(self.top, other.top)

        if x1 >= x2 or y1 >= y2:
            return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.left, other.left)
        y1 = min(self.bottom, other.bottom)
        x2 = max(self.right, other.right)
        y2 = max(self.top, other.top)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        midx = (self.left + self.right) / 2
        midy = (self.bottom + self.top) / 2

        A = Rectangle(self.left, self.bottom, midx, midy)
        B = Rectangle(midx, self.bottom, self.right, midy)
        C = Rectangle(midx, midy, self.right, self.top)
        D = Rectangle(self.left, midy, midx, self.top)

        return (A, B, C, D)
