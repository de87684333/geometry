import pytest
from geometry import area, perimeter

def test_area_basic():
	assert area(3, 4) == 12

def test_perimeter_basic():
	assert perimeter(3, 4) == 14

def test_zero_dimensions():
	assert area(0, 5) == 0
	assert perimeter(0, 5) == 10

def test_negative_dimensions_raise():
	with pytest.raises(ValueError):
		area(-1, 2)
	with pytest.raises(ValueError):
		perimeter(1, -2)
