from flask import Flask
from services.sesion import ws_sesion
from services.rol import ws_rol
from services.sede import ws_sede


#Create app variable with Flask
app = Flask(__name__)

#Register modules contains web services
app.register_blueprint(ws_sesion)
app.register_blueprint(ws_rol)
app.register_blueprint(ws_sede)


@app.route('/')
def home():
    return 'Web Services Running'


#Start web services
if __name__ == '__main__':
    app.run(port=3001, debug=True, host='0.0.0.0')
