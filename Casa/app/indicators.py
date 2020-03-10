
class Indicator:
  def __init__(self, label, indicator_id, room, slave, address):
    self.label = label
    self.id = indicator_id
    self.room = room
    self.slave = slave
    self.address = address
    self.menu_items = [{'handler':"configure()", 'label':'Configurar'},
                       {'handler':"closeMenu()", 'label':'Cerrar'}]

  def getValue(self):
    return self.slave.getValue(self.address)

    
class Tank(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address, min_level, capacity):
    super(Tank, self).__init__(label, indicator_id, room_id, slave, address)
    self.min_level = min_level
    self.capacity = capacity
                       
  # def getValue(self):
  #   from random import randint
  #   return randint(0,100)
    
class LowerTank(Tank):
  def __init__(self, label, indicator_id, room_id, slave, address, min_level, capacity):
    super(LowerTank, self).__init__(label, indicator_id, room_id, slave, address, min_level, capacity)
    self.type = "LowerTank"
    
class UpperTank(Tank):
  def __init__(self, label, indicator_id, room_id, slave, address, min_level, capacity):
    super(UpperTank, self).__init__(label, indicator_id, room_id, slave, address, min_level, capacity)
    self.type = "UpperTank"
    
class Pump(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address, ackAdr):
    super(Pump, self).__init__(label, indicator_id, room_id, slave, address)
    self.menu_items += [{'handler':"start()", 'label':'Llenar'},
                   {'handler':"stop()", 'label':'Detener'},
                   {'handler':"ack()", 'label':'Rearmar'}]
    self.type = "Pump"
    self.ackAdr = ackAdr
  
  def ack_error(self):
    self.slave.instrument.write_register(self.ackAdr, 1)
    
class Pir(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Pir, self).__init__(label, indicator_id, room_id, slave, address)
    self.type = "Pir"
    
class Ldr(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Ldr, self).__init__(label, indicator_id, room_id, slave, address)
    self.type = "Ldr"
                       
  # def getValue(self):
  #   from random import randint
  #   return randint(0,100)
    
class Light(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Light, self).__init__(label, indicator_id, room_id, slave, address)
    self.type = "Light"
    
class Door(Indicator):
  def __init__(self, label, indicator_id, room_id, slave, address):
    super(Door, self).__init__(label, indicator_id, room_id, slave, address)
    self.type = "Door"
