import pytest
from triangle.triangle import Triangle


@pytest.fixture()
def set_triangle():
    triangle = Triangle(9, 8, 7)
    yield triangle
    del triangle


@pytest.fixture()
def right_triangle():
    right_tr = Triangle(6, 6, 6)
    yield right_tr
    del right_tr


@pytest.fixture()
def rb_triangle():
    rb_triangle = Triangle(5, 5, 7)
    yield rb_triangle
    del rb_triangle


@pytest.fixture()
def right_angled_triangle():
    ra_triangle = Triangle(3, 4, 5)
    yield ra_triangle
    del ra_triangle
