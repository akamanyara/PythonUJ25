from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

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

    def center(self):
        return Point(
            (self.pt1.x + self.pt2.x) / 2,
            (self.pt1.y + self.pt2.y) / 2
        )

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        return Rectangle(
            self.pt1.x + x,
            self.pt1.y + y,
            self.pt2.x + x,
            self.pt2.y + y,
        )

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 >= x2 or y1 >= y2:
            return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        midx = (self.pt1.x + self.pt2.x) / 2
        midy = (self.pt1.y + self.pt2.y) / 2

        A = Rectangle(self.pt1.x, self.pt1.y, midx, midy)
        B = Rectangle(midx, self.pt1.y, self.pt2.x, midy)
        C = Rectangle(midx, midy, self.pt2.x, self.pt2.y)
        D = Rectangle(self.pt1.x, midy, midx, self.pt2.y)

        return (A, B, C, D)