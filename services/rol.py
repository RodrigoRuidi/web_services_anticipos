# Web services Rol
from flask import Blueprint, request, jsonify
from models.rol import Rol
import json
import validar_token as vt

ws_rol = Blueprint('ws_rol', __name__)

@ws_rol.route('/rol/listar', methods=['POST'])
@vt.validar_token
def listado_roles():
    if request.method == 'POST':
        obj = Rol()
        rpta_rol = obj.listar_roles()
        datos = json.loads(rpta_rol)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
