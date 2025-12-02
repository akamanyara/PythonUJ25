import pytest
from rectangles import Rectangle
from points import Point

def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    r = Rectangle.from_points((p1, p2))
    assert r.left == 1
    assert r.top == 6

def test_properties_coordinates():
    r = Rectangle(1, 2, 4, 6)
    assert r.left == 1
    assert r.right == 4
    assert r.bottom == 2
    assert r.top == 6
    assert r.width == 3
    assert r.height == 4

def test_corner_points():
    r = Rectangle(1, 2, 4, 6)
    assert r.topleft == Point(1, 6)
    assert r.topright == Point(4, 6)
    assert r.bottomleft == Point(1, 2)
    assert r.bottomright == Point(4, 2)

def test_center():
    r = Rectangle(0, 0, 4, 4)
    assert r.center == Point(2, 2)

def test_area():
    assert Rectangle(1, 1, 4, 6).area() == 15

def test_move():
    r = Rectangle(1, 1, 4, 4).move(2, 3)
    assert r == Rectangle(3, 4, 6, 7)

def test_intersection():
    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(2, 2, 6, 6)
    inter = r1.intersection(r2)
    assert inter == Rectangle(2, 2, 4, 4)

def test_no_intersection():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(3, 3, 5, 5)
    assert r1.intersection(r2) is None

def test_cover():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(1, 1, 4, 3)
    cov = r1.cover(r2)
    assert cov == Rectangle(0, 0, 4, 3)

def test_make4():
    r = Rectangle(0, 0, 4, 4)
    A, B, C, D = r.make4()
    assert A == Rectangle(0, 0, 2, 2)
    assert B == Rectangle(2, 0, 4, 2)
    assert C == Rectangle(2, 2, 4, 4)
    assert D == Rectangle(0, 2, 2, 4)
