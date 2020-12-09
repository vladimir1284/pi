
class Indicator:
  configDir = {}
  def __init__(self, label, indicator_id, room, slave, address, configAdr):
    self.label = label
    self.id = indicator_id
    self.room = room
    self.slave = slave
    self.address = address
    self.configAdr = configAdr
    self.menu_items = []

  def getValue(self):
    return self.slave.getValue(self.address)

  def getConfig(self, key):
    return self.slave.getConfig(self.configDir[key])

    
class Tank(Indicator):
  configDir = {"height":0,
               "gap":1,
               "min":2,
               "restart":3}
  def __init__(self, label, indicator_id, room_id, slave, address, configAdr, min_level, capacity):
    super(Tank, self).__init__(label, indicator_id, room_id, slave, address, configAdr)
    self.min_level = min_level
    self.capacity = capacity    
    self.menu_items = [{'handler':"configure()", 'label':'Configurar'},
                       {'handler':"closeMenu()", 'label':'Cerrar'}]
    
class LowerTank(Tank):
  def __init__(self, label, indicator_id, room_id, slave, address, configAdr, min_level, capacity):
    super(LowerTank, self).__init__(label, indicator_id, room_id, slave, address, configAdr, min_level, capacity)
    self.type = "LowerTank"
    
class UpperTank(Tank):
  def __init__(self, label, indicator_id, room_id, slave, address, configAdr, min_level, capacity):
    super(UpperTank, self).__init__(label, indicator_id, room_id, slave, address, configAdr, min_level, capacity)
    self.type = "UpperTank"
    
class Pump(Indicator):
  configDir = {"start_capacitor":0,
               "max_time_on":1,
               "full_tank":2}
  def __init__(self, label, indicator_id, room_id, slave, address, configAdr, ackAdr):
    super(Pump, self).__init__(label, indicator_id, room_id, slave, address, configAdr)
    self.menu_items += [{'handler':"start()", 'label':'Llenar'},
                   {'handler':"stop()", 'label':'Detener'},
                   {'handler':"ack()", 'label':'Rearmar'},
                   {'handler':"configure()", 'label':'Configurar'},
                   {'handler':"closeMenu()", 'label':'Cerrar'}]
    self.type = "Pump"
    self.ackAdr = ackAdr
  
  def ack_error(self):
    self.slave.instrument.write_register(self.ackAdr, 1)
    
class Pir(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Pir, self).__init__(label, indicator_id, room_id, slave, address, 0)
    self.type = "Pir"
    
class Ldr(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Ldr, self).__init__(label, indicator_id, room_id, slave, address, 0)
    self.type = "Ldr"
                      
class Light(Indicator):
  configDir = {"light_mode":0,
               "sleep_time":1,
               "smart":2,
               "smart_delay":3,
               "init_delay":4,
               "delay_increment":5,
               "luminosity_threshold":6}
  def __init__(self, label, indicator_id, room_id, slave, address, configAdr):
    super(Light, self).__init__(label, indicator_id, room_id, slave, address, configAdr)
    self.type = "Light"
    self.menu_items = [{'handler':"active()", 'label':"Activa"},
                       {'handler':"turnOn()", 'label':'Encendida'},
                       {'handler':"courtesy()", 'label':'Cortesía'},
                       {'handler':"turnOff()", 'label':'Apagada'},
                       {'handler':"configure()", 'label':'Configurar'},
                       {'handler':"closeMenu()", 'label':'Cerrar'}]
    
class Door(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Door, self).__init__(label, indicator_id, room_id, slave, address, 0)
    self.type = "Door"
