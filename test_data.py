from decimal import Decimal

def generate_test_data():
    from manager import generate_uuid
    projects = [
        {
            'uuid': generate_uuid(),
            'name': 'Plastic Free Pals',
            'latitude': Decimal(37.983810),
            'longitude': Decimal(23.727539), # Athens, GR

        },
        {
            'uuid': generate_uuid(),
            'name': 'Green Shipping Solutions',
            'latitude': Decimal(37.577870),
            'longitude': Decimal(-122.348090), # Burlingame, CA

        },
        {
            'uuid': generate_uuid(),
            'name': 'Arboreal Initiatives',
            'latitude': Decimal(49.246292),
            'longitude': Decimal(-123.116226), # Vancouver, CAN

        },
        {
            'uuid': generate_uuid(),
            'name': 'Zero Waste Restaurant Supplies',
            'latitude': Decimal(37.668819),
            'longitude': Decimal(-122.080795), # Hayward, CA

        },
    ]
    return projects