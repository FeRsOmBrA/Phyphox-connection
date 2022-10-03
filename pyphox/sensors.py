from typing import Any

#Esta clase se usa para requerir los datos de los sensores,  no se ha utilzado para el desarrollo del proyecto, ya que el programa obtiene los datos directamente de la medicion de cada celular, sin embargo, pueden usarla para #requerir cierto valor X, Y, o Z o varios a la vez, el tiempo, o para los sensores que manejan un solo valor 

class Sensor:
    """Representa un sensor Phyphox"""

    __slots__ = ('prefix', 'phyphox')
    prefix: str
    phyphox: Any

    def __init__(self, phyphox: Any, prefix: str) -> None:
        self.prefix = prefix
        self.phyphox = phyphox

    def get(self, var: str) -> float:
        """Devuelve el valor 'var' del sensor desde phyphox sensors_data"""
        return self.phyphox.sensors_data[self.prefix+var]

    def get_time(self) -> float:
        """Devuelve el valor del tiempo del sensor de phyphox sensors_data"""
        return self.get('_time')

    def include_time(self) -> None:
        """Las siguientes llamadas a Fetch() obtendrán la hora del sensor"""
        self.phyphox.query += self.prefix + '_time&'


class XYZSensor(Sensor):
    """Representa un sensor con variables X, Y y Z"""

    def get_x(self) -> float:
        """Devuelve el valor X del sensor de phyphox sensors_data"""
        return self.get('X')

    def get_y(self) -> float:
        """Devuelve el valor Y del sensor de phyphox sensors_data"""
        return self.get('Y')

    def get_z(self) -> float:
        """Devuelve el valor Z del sensor de phyphox sensors_data"""
        return self.get('Z')

    def include_x(self) -> None:
        """Las siguientes llamadas a Fetch() obtendrán el valor X del sensor"""
        self.phyphox.query += self.prefix + 'X&'

    def include_y(self) -> None:
        """Las siguientes llamadas a Fetch() obtendrán el valor X del sensor"""
        self.phyphox.query += self.prefix + 'Y&'

    def include_z(self) -> None:
        """Las siguientes llamadas a Fetch() obtendrán el valor X del sensor"""
        self.phyphox.query += self.prefix + 'Z&'

    def include_all(self) -> None:
        """Las siguientes llamadas a Fetch() recuperarán todos los datos del sensor además del tiempo"""
        self.phyphox.query += (self.prefix + 'X&' +
                               self.prefix + 'Y&' +
                               self.prefix + 'Z&')


class VSensor(Sensor):
    """Representa un sensor de un solo valor"""

    def get_value(self) -> float:
        """Devuelve el valor del sensor de phyphox sensors_data"""
        return self.phyphox.sensors_data[self.prefix]
