from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from app.config import *
from serial import Serial

class RoomForm(FlaskForm):
    label = StringField(Strings.label, validators=[DataRequired()])
    submit = SubmitField(Strings.save)

class PortForm(FlaskForm):
    port_choices = (("/dev/ttyUSB0","/dev/ttyUSB0"),("/dev/tty2","/dev/tty2"))
    port = SelectField(Strings.port, choices = port_choices,  default="/dev/ttyUSB0")
    baudrate_choices = [(x,x) for x in Serial.BAUDRATES]
    baudrate = SelectField(Strings.baudrate, choices = baudrate_choices,  default=19200, coerce=int)
    databits_choices = [(x,x) for x in Serial.BYTESIZES]
    databits = SelectField(Strings.databits, choices = databits_choices,  default=8, coerce=int)
    parity_choices = [(x,x) for x in Serial.PARITIES]
    parity = SelectField(Strings.parity, choices = parity_choices,  default='N')
    stopbits_choices = [(x,x) for x in Serial.STOPBITS]
    stopbits = SelectField(Strings.stopbits, choices = stopbits_choices,  default=1, coerce=float)
    
    submit = SubmitField(Strings.save)

class SlaveForm(FlaskForm):
    label = StringField(Strings.label, validators=[DataRequired()])
    port_choices = [(port.port, port.port) for port in ports]
    port = SelectField(Strings.port, choices = port_choices)
    slaveAdr = DecimalField(Strings.slaveAdr, places = 0, 
                validators=[NumberRange(min=1,max=255,
                message="Slave address must be in the range [1,255]")])
    setupsAdr = DecimalField(Strings.registersAdr, places = 0, 
                validators=[NumberRange(min=0,max=65535,
                message="Register addresses must be in the range [0,65535]")])
    setupsCount = DecimalField(Strings.registersCount, places = 0, 
                validators=[NumberRange(min=0,max=999)])
    variablesAdr = DecimalField(Strings.registersAdr, places = 0, 
                validators=[NumberRange(min=0,max=65535,
                message="Register addresses must be in the range [0,65535]")])
    variablesCount = DecimalField(Strings.registersCount, places = 0, 
                validators=[NumberRange(min=0,max=999)])
    submit = SubmitField(Strings.save)

class IndicatorForm(FlaskForm):
    label = StringField(Strings.label, validators=[DataRequired()])
    type_choices = [(key,Strings.typesDict[key]) for key in Strings.typesDict]
    type = SelectField(Strings.type, choices = type_choices)    
    room_choices = [(room.id, room.label) for room in rooms]
    room = SelectField(Strings.room, choices = room_choices)
    slave_choices = [(slave.id, slave.label) for slave in slaves]
    slave = SelectField(Strings.node, choices = slave_choices)    
    address = DecimalField(Strings.registersAdr, places = 0, 
                validators=[NumberRange(min=0,max=65535,
                message="Register addresses must be in the range [0,65535]")])
    submit = SubmitField(Strings.save)

class TankForm(FlaskForm):
    min_level = DecimalField(Strings.min_level, places = 0,                  
                        validators=[NumberRange(min=0,max=100)])
    capacity = DecimalField(Strings.capacity, places = 0,
                        validators=[NumberRange(min=0,max=99999)])
    height = DecimalField(Strings.height, places = 0,
                        validators=[NumberRange(min=20,max=300)])
    gap = DecimalField(Strings.gap, places = 0,
                        validators=[NumberRange(min=15,max=100)])
    min = DecimalField(Strings.min, places = 0,
                        validators=[NumberRange(min=0,max=100)])
    restart = DecimalField(Strings.restart, places = 0,                  
                        validators=[NumberRange(min=0,max=100)])
    submit = SubmitField(Strings.save)

class PumpForm(FlaskForm):
    start_choices = ((2,"2s"),(3,"3s"),(4,"4s"),(5,"5s"))
    start_capacitor = SelectField(Strings.start_capacitor, choices = start_choices, 
                                    coerce=int, validators=[DataRequired()]) 
    max_time_on = DecimalField(Strings.max_time_on, places = 0,                  
                        validators=[NumberRange(min=1,max=60)])
    full_tank = DecimalField(Strings.full_tank, places = 0,                  
                        validators=[NumberRange(min=30,max=100)])
    submit = SubmitField(Strings.save)

class LightForm(FlaskForm):
    sleep_time = DecimalField(Strings.sleep_time, places = 0,                  
                        validators=[NumberRange(min=0,max=900)])
    smart_choices = ((1,"Activo"),
                    (0,"Inactivo"))                
    smart = SelectField(Strings.smart, choices = smart_choices, 
                                    coerce=int) 
    smart_delay = DecimalField(Strings.smart_delay, places = 0,                  
                        validators=[NumberRange(min=10,max=30)])
    init_delay = DecimalField(Strings.init_delay, places = 0,                  
                        validators=[NumberRange(min=30,max=900)])
    delay_increment = DecimalField(Strings.delay_increment, places = 0,                  
                        validators=[NumberRange(min=30,max=900)])
    luminosity_threshold = DecimalField(Strings.luminosity_threshold, places = 0,                  
                        validators=[NumberRange(min=0,max=100)])
    submit = SubmitField(Strings.save)

    
    
    
    
    
    
    