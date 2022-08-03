from enum import Enum

class DistanceUnit(Enum):
    """
    For use by haversine in distance calculation
    """
    MILES = "mi"
    KILOMETERS = "ki"


class Limit(Enum):
    """
    For use by queries
    """
    LOW = "50"
    MEDIUM = "75"
    HIGH = "100"