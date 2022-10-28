from flask import request, jsonify
import jwt
from functools import wraps
from config import SecretKey
import json
from models.sesion import Sesion


def validar_estado_token(id):
    obj = Sesion()
    rpta = obj.validar_estado_token(id)
    datos = json.loads(rpta)
    if datos['status']:
        estado_token = datos['data']['estado_token']
        if estado_token == None:
            return False
        else:
            return estado_token != '0'
    else:
        return False

# Wrapper function
def validar_token(fx):
    @wraps(fx)
    def envoltura():

        if not 'token' in request.form:
            return jsonify({'status': False, 'data': '', 'message': 'Falta token'}), 403

        token = request.form['token']

        if not token:
            return jsonify({'status': False, 'data': '', 'message': 'Falta token'}), 403

        try:
            data = jwt.decode(token, SecretKey.JWT_SECRET_JEY,
                              algorithms='HS256')

            # Extract user id
            id = data['user_id']

            # Validate token status
            estado_token = validar_estado_token(id)

            if estado_token == False:
                return jsonify({'status': False, 'data': '', 'message': 'Token inactivo'}), 403
        except (jwt.DecodeError, jwt.ExpiredSignatureError) as error:
            return jsonify({'status': False, 'data': '', 'message': format(error)}), 403
        except (Exception) as error:
            return jsonify({'status': False, 'data': '', 'message': format(error)}), 403

        return fx()
    return envoltura

