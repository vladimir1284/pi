from flask import render_template, make_response, request, jsonify, url_for, redirect, flash
from app import app
from app.config import *
from app.forms import *

 # ------------------------ Default ----------------------------
default_room = taller
current_room = default_room
room_indicators = [x for x in indicators if x.room == current_room]

@app.route('/')
@app.route('/index')
def index():  
  return redirect(url_for('room',room_id=current_room.id))
# -------------------------------------------------------------


@app.route('/favicon.ico')
def favicon():  
  return redirect('/static/img/favicon.ico')
  
@app.route('/room/<room_id>')
def room(room_id):  
  for room in rooms:
    if room.id == room_id:
      break
  current_room = room
  room_indicators = [x for x in indicators if x.room == room]
  return render_template('index.html', rooms = rooms, room = room,
                          indicators = room_indicators, strings=Strings)
  
@app.route('/objects.js')
def objects():  
  return render_template('objects.js', indicators = room_indicators, room = current_room.id)
  
@app.route('/get_indicators_data', methods=['POST', 'GET'])
def get_indicators_data(): 
    room = request.get_json()
    data = []
    for indicator in indicators:
      if (indicator.room.id == room):
        data.append({'indicator':indicator.id,'value':indicator.getValue()})
    res = jsonify(data = data)
    print(res)
    return res

# -------------------------- Configurations ---------------------------
@app.route('/config')
def config():  
  return render_template('config.html', rooms = rooms, slaves = slaves,
                          ports=ports, indicators = indicators, strings=Strings)

@app.route('/room_edit', methods=['GET', 'POST'])
@app.route('/room_edit/<room_id>', methods=['GET', 'POST'])
def room_edit(room_id=""):
  if room_id != "":
    for room in rooms:
      if room.id == room_id:
        break
    form = RoomForm(label = room.label)
  else:
    form = RoomForm()

  if form.validate_on_submit():
    flash(Strings.modified+' {}'.format(form.label.data))
    return redirect('/config')
    
  return render_template('edit_room.html', title=Strings.room, form=form, strings=Strings, 
                          rooms = rooms)

@app.route('/port_edit', methods=['GET', 'POST'])
@app.route('/port_edit/<port>', methods=['GET', 'POST'])
def port_edit(port=""):
  if port != "":
    for port in ports:
      if port.port == port:
        break
    form = PortForm(port = port.port)
  else:
    form = PortForm()

  if form.validate_on_submit():
    flash(Strings.modified+' {}'.format(form.port.data))
    return redirect('/config')
    
  return render_template('edit_port.html', title=Strings.port, form=form, 
                          strings=Strings, rooms = rooms)


@app.route('/slave_edit', methods=['GET', 'POST'])
@app.route('/slave_edit/<slave_id>', methods=['GET', 'POST'])
def slave_edit(slave_id=""):
  if slave_id != "":
    for slave in slaves:
      if slave.id == slave_id:
        break
    form = SlaveForm(label = slave.label, 
                      port = slave.port.port,
                      slaveAdr =  slave.slave_address,
                      setupsAdr = slave.setupsAdr,
                      setupsCount = slave.setupsCount,
                      variablesAdr = slave.variablesAdr,
                      variablesCount = slave.variablesCount)
  else:
    form = SlaveForm()

  if form.validate_on_submit():
    flash(Strings.modified+' {}'.format(form.label.data))
    return redirect('/config')
    
  return render_template('edit_slave.html', title=Strings.node, form=form, 
                          strings=Strings, rooms = rooms)


@app.route('/indicator_edit', methods=['GET', 'POST'])
@app.route('/indicator_edit/<indicator_id>', methods=['GET', 'POST'])
def indicator_edit(indicator_id=""):
  if indicator_id != "":
    for indicator in indicators:
      if indicator.id == indicator_id:
        break
    form = IndicatorForm(label = indicator.label, 
                      type = indicator.type, 
                      room = indicator.room.id, 
                      slave = indicator.slave.id,
                      address = indicator.address)
  else:
    form = IndicatorForm()

  if form.validate_on_submit():
    flash(Strings.modified+' {}'.format(form.label.data))
    print(form.type.data)
    return redirect('/config')
    
  return render_template('edit_indicator.html', title=Strings.node, form=form, 
                          strings=Strings, rooms = rooms)