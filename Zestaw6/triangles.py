from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self):
        return (
            f"Triangle({self.pt1.x}, {self.pt1.y}, "
            f"{self.pt2.x}, {self.pt2.y}, "
            f"{self.pt3.x}, {self.pt3.y})"
        )

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return False

        points_self = [self.pt1, self.pt2, self.pt3]
        points_other = [other.pt1, other.pt2, other.pt3]

        return sorted(points_self, key=lambda p: (p.x, p.y)) == \
               sorted(points_other, key=lambda p: (p.x, p.y))

    def __ne__(self, other):
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        cy = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(cx, cy)

    def area(self):
        return abs(
            (self.pt1.x * (self.pt2.y - self.pt3.y) +
             self.pt2.x * (self.pt3.y - self.pt1.y) +
             self.pt3.x * (self.pt1.y - self.pt2.y)) / 2
        )

    def move(self, x, y):
        for pt in (self.pt1, self.pt2, self.pt3):
            pt.x += x
            pt.y += y