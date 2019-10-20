import socketio
import eventlet
import base64
import machine_learning

#HOST = '192.168.1.26'
#HOST = '169.254.9.115'
HOST = '172.20.10.2'
PORT = 8080

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def photo(sid, data):
    with open("image.jpg", "wb") as fh:
        fh.write(base64.decodebytes(data))
        preds = machine_learning.predictImageClasse()
        sio.emit('nav_instructions', {'predictions' : 'todo'})

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((HOST, PORT)), app)
