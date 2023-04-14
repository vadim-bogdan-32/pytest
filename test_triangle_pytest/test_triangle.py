from triangle.triangle import Triangle
import pytest


@pytest.mark.parametrize('a, b, c',
                         [(7, 8, 9), (9, 7, 8)])
def test_triangle_eq(a, b, c):
    first = Triangle(a, b, c)
    second = Triangle(9, 8, 7)
    assert first == second


def test_triangle_lt(set_triangle):
    first = set_triangle
    second = Triangle(12, 11, 10)
    assert first < second


def test_right_triangle(right_triangle):
    assert right_triangle.is_right_triangle()


def test_rb_triangle(rb_triangle):
    assert rb_triangle.two_sides_eq()

@pytest.mark.xfail(reason='bug in triangle class')
def test_right_angled_triangle(right_angled_triangle):
    assert right_angled_triangle.is_right_angled()

