import pytest
from app import check

def test_inside_geo_fence():
    center_lat = 80.09734748801102
    center_lon = 12.919357753640268
    lat = 80.09738668239515
    lon = 12.919405460455502
    assert check(center_lat, center_lon, lat, lon) == True

def test_outside_geo_fence():
    center_lat = 80.09734748801102
    center_lon = 12.919357753640268
    lat = 80.09750000000000
    lon = 12.91950000000000
    assert check(center_lat, center_lon, lat, lon) == False
