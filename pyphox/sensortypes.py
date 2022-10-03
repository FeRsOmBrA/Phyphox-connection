from enum import Enum

# Aqui se definen los tipos de sensores
class SensorType(Enum):
    ACCELEROMETER = {"type": "XYZ", "name": "accelerometer", "prefix": "acc"}
    GYROSCOPE = {"type": "XYZ", "name": "gyroscope", "prefix": "gyr"}
    LINEAR_ACCELERATION = {"type": "XYZ", "name": "linear_acceleration", "prefix": "lin"}
    MAGNETIC_FIELD = {"type": "XYZ", "name": "magnetic_field", "prefix": "mag"}
    LIGHT = {"type": "V", "name": "light", "prefix": "illum"}
    PROXIMITY = {"type": "V", "name": "proximity", "prefix": "prox"}
