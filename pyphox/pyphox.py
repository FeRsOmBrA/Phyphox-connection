

import json
import os
from typing import Any
from urllib.request import urlopen
import requests
from .sensortypes import SensorType
from .sensors import Sensor, VSensor, XYZSensor
from tkinter import filedialog
import os
import win32com.client as client

# clase Pyphox


class Pyphox:
    '''Representa una conexión con el servidor remoto y controla el experimento'''

    __slots__ = ('address', 'query', 'sensors', 'sensors_data', 'output_format', 'name', 'file_id')

    address: str
    query: str
    sensors: list[str]
    sensors_data: set[str, float]
    output_format: str
    file_id: str
    name: str


    def __init__(self, address: str, sensors: list[str]):
        self.address = address
        self.sensors = sensors
        self.query = ""
        self.sensors_data = []

    def register_sensor(self, sensor: SensorType) -> Sensor:
        '''
        Devuelve XYZSensor o VSensor representando un sensor en el experimento.
        Dado que VSensor sólo tiene una variable, será automáticamente
        obtenido con Fetch()
        Como XYZSensor tiene varias variables, ninguna será obtenida con Fetch().
        Para obtener los datos del sensor, IncludeX, IncludeY o IncludeZ
        debe ser llamado.
        '''
        if not self.has_sensor(sensor):
            return None

        prefix = sensor.value['prefix']
        stype = sensor.value['type']
        if stype == 'XYZ':
            return XYZSensor(self, prefix)

        if stype == 'V':
            self.query += prefix + "&"
            return VSensor(self, prefix)

        return None

    def has_sensor(self, sensor: SensorType) -> bool:
        '''Devuelve True si el experimento utiliza el tipo de sensor dado, si no, False'''
        return sensor.value['name'] in self.sensors

    def execute(self, command: str) -> dict[str, Any]:
        '''Ejecuta algún comando remoto en el host. Devuelve el resultado JSON
           resultado del comando'''
        resp = urlopen(self.address + command)
        data = json.load(resp)
        resp.close()

        return data

    def fetch(self) -> None:
        '''Solicita al host remoto los datos más recientes. Los datos se
           guardados en el campo SensorsData'''
        res = self.execute("/get?" + self.query)

        data = {}
        for k, v in res["buffer"].items():
            data[k] = v["buffer"][0]

        self.sensors_data = data
    def start(self) -> bool:
        '''Inicia la medición. Por defecto, Fetch() se llama automáticamente'''
        res = self.execute("/control?cmd=start")
        self.fetch()
        return res["result"]

    def stop(self) -> bool:
        '''Deja de medir'''
        res = self.execute("/control?cmd=stop")
        return res["result"]

    def clear(self) -> bool:
        '''Borra el buffer del experimento'''
        res = self.execute("/control?cmd=clear")
        return res["result"]
    def export(self, format: str ) :
        '''
          Exporta los datos en el formato indicado, por ahora solo csv o excel.
           
          :param format: 

          `csv` -->
          Se guarda un archivo en formato zip con los datos y se extrae en una carpeta llamada  `datos`, en esta carpeta
          se encuentra un archivo llamado `Accelerometer.csv` con los datos de los sensores y otra carpeta llamada `meta` con informacion del dispositivo medidor
          y los sensores que se usaron en el experimento.

          `excel` -->
          Se guarda un archivo en formato xls con todos los datos de los sensores y otras hoja adicionales con informacion del dispositivo medidor
          
  
        '''
        self.output_format = format
        
        if format == 'csv':
            pass  # Actualmente en desarrollo

            return print('Se han exportado los datos a csv') 
        elif format == 'excel':
            
            url =  self.address + '/export?format=0'
            name=  self.address.split(':')[1].split('/')[2]
            # pedir al usuario la ruta del archivo
            global path
            path = filedialog.askdirectory()
            # descargar el archivo
            r = requests.get(url, allow_redirects=True)
            open(f'{path}/{name}.xls', 'wb').write(r.content)
            excel = client.DispatchEx("Excel.Application")
            # convertir el archivo a xlsx
            for file  in os.listdir( path ):
                filename, file_extension = os.path.splitext(file)
                print(filename, file_extension)
                wb = excel.Workbooks.Open(f'{path}/{file}')
                output_path_bad = f'{path}/{filename}.xlsx'
                output_path = output_path_bad.replace('/', '\\' )
                wb.SaveAs(output_path, FileFormat = 51)
                wb.Close()
                if file_extension == '.xls':
                    os.remove(f'{path}/{file}')
                    
            excel.Quit()
            self.name = name
        else:
            return print('Error, formato no soportado')

    def read(self) -> None:
        
        '''
        Abre el archivo en una nueva ventana de excel

        '''
        if self.output_format == 'csv':
           pass  # Primero tenemos que configurar la exportación de csv
        elif self.output_format == 'excel':
            os.startfile(f'{self.name}.xlsx')



        

# conectar la función principal
        
def connect(address: str) -> Pyphox:
    '''Connects to the remote experiment at the given address'''
    address = "http://" + address
    config_resp = urlopen(address + "/config")

    sensors = []
    for inp in json.load(config_resp)['inputs']:
        sensor = inp['source']
        sensors.append(sensor)

    config_resp.close()

    return Pyphox(address, sensors)