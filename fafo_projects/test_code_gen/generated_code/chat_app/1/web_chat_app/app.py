import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@socketio.on('message')
def handle_message(data):
    flask_socketio.send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)