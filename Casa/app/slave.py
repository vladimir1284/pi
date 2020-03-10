from minimalmodbus import Instrument
from serial import Serial
import traceback

class Slave:
  def __init__(self, label, slave_id, slave_address, setupsAdr, 
                setupsCount, variablesAdr, variablesCount, port):
    self.label          = label
    self.id             = slave_id
    self.port           = port
    self.slave_address  = slave_address
    self.setupsAdr      = setupsAdr
    self.setupsCount    = setupsCount
    self.variablesAdr   = variablesAdr
    self.variablesCount = variablesCount

    try:
      self.instrument = Instrument(self.port, slave_address)
    except:
      self.status = "ERROR"
      traceback.print_exc()

    self.status = "NEW"
    self.variable_values = []
    self.config_values = []

  def getConfig(self, adr):
    if self.status == "NEW":
      self.getConfigs()
    if self.status == "OK":
      return self.config_values[adr]
    else:
      return 0

  def getValue(self, adr):
    if self.status == "OK":
      return self.variable_values[adr-self.variablesAdr]
    else:
      return 0

  def getVariables(self):
    try:
      self.variable_values = self.instrument.read_registers(self.variablesAdr, self.variablesCount)
      self.status = "OK"
    except IOError:
      self.status = "ERROR"
      traceback.print_exc()

  def getConfigs(self):
    try:
      self.config_values = self.instrument.read_registers(self.setupsAdr, self.setupsCount)
      self.status = "OK"
    except IOError:
      self.status = "ERROR"
      traceback.print_exc()

  def setConfigs(self):
    try:
      self.instrument.write_registers(self.setupsAdr, self.config_values)
      self.status = "OK"
    except IOError:
      self.status = "ERROR"
      traceback.print_exc()

  def run(self):
    if self.status != "OK":
        self.getConfigs()
    self.getVariables()

  def simulate(self):
    print('Simulating from slave: %s' % self.id)
    from random import randint
    self.variable_values = [randint(0,100) for i in range(self.variablesCount)]
    self.status = "SIMULATE"