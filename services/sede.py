# Web services Rol
from flask import Blueprint, request, jsonify
from models.sede import Sede
import json
import validar_token as vt

ws_sede = Blueprint('ws_sede', __name__)

@ws_sede.route('/sede/listar', methods=['POST'])
@vt.validar_token
def listado_roles():
    if request.method == 'POST':
        obj = Sede()
        rpta_sedes = obj.listar_sedes()
        datos = json.loads(rpta_sedes)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
