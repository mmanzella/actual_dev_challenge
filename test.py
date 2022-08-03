import pytest
from test_data import generate_test_data


def test_uuid_generator():
    from manager import generate_uuid
    uuid = generate_uuid()
    assert uuid

def test_calculate_distance():
    from manager import calculate_distance
    projects = generate_test_data()
    import pdb
    pdb.set_trace()

    coord_0 = projects[0]['latitude'], projects[0]['longitude']
    coord_1 = projects[1]['latitude'], projects[1]['longitude']
    distance = calculate_distance(coord_0, coord_1)


