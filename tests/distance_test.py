# tests/distance_test.py
from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(23,11,35,2)) == float