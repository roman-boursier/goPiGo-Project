import socketio
import base64

sio = socketio.Client()

@sio.event
def connect():
	print('connection established')

@sio.event
def nav_instructions(data):
	print('message received with ', data)
	# sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
	print('disconnected from server')

def sendPhotoToServer(photoPath):
	b64 = base64.encodestring(open(photoPath,"rb").read())
	sio.emit('photo', b64)
	print('sending image')

def start():
	sio.connect('http://172.20.10.2:8080')
	#self.sio.connect('http://169.254.9.115:8080')

sio.wait()