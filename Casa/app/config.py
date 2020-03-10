import os
from app.indicators import *
from app.room import Room
from app.slave import Slave
from serial import Serial

class Config(object):
    SCHEDULER_API_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class Strings(object):
    room = "Habitación"
    rooms = "Habitaciones"
    label = "Etiqueta"
    save = 'Guardar'
    ports = "Puertos"
    port = "Puerto"
    slaves = "Modbus"
    baudrate = "Velocidad"
    configuration = "Configuración"
    configurations = "Configuraciones"
    node = "Nodo"
    nodes = "Nodos"
    address = "Dirección"
    variables = "Variables"
    indicators = "Indicadores"
    type = "Tipo"
    modified = "Modificado correctamente"
    databits = "Bits de datos"
    parity = "Paridad"
    stopbits = "Bits de parada"
    slaveAdr = "Dirección del esclavo"
    registersAdr = "Dirección del primer registro"
    registersCount = "Cantidad de registros"
    min_level = 'Nivel de seguridad (%)'
    capacity = 'Capacidad (lts)'
    height = 'Altura del tanque (cm)'
    gap = 'Brecha superior (cm)'
    min = 'Nivel mínimo (%)'
    restart = 'Nivel de reinicio (%)'

    typesDict = {
        "LowerTank":"Cisterna",
        "UpperTank":"Tanque elevado",
        "Pump":"Bomba",
        "Pir":"Sensor de movimiento",
        "Ldr":"Sensor de luminosidad",
        "Light":"Luminaria",
        "Door":"Sensor de puerta"}

port1 = Serial(port="/dev/tty2",baudrate=19200)
ports = [port1]

slave1 = Slave("Taller", "taller", 1, 0, 18, 18, 7, port1)
slaves = [slave1]

cameras = Room('Camaras', 'cameras')
taller = Room('Taller', 'taller')
rooms =[cameras, taller]
         
tanque   = UpperTank("Tanque", "upperTank0", taller, slave1, 18, min_level = 25, capacity=500)
cisterna = LowerTank("Cisterna", "lowerTank0", taller, slave1, 19, min_level = 25, capacity=200)
bomba = Pump("Bomba", "pump0", taller, slave1, 20, 21)
pir0 = Pir("PIR Taller", "pir0", taller, slave1, 23)
ldr0 = Ldr("Luminosidad Taller", "ldr0", taller, slave1, 22)
light0 = Light("Luz Taller", "light0", taller, slave1, 24)
door0 = Door("Puerta del Taller", "door0", taller, slave1, 23)
  
indicators = [tanque, cisterna, bomba, pir0, ldr0, light0, door0]