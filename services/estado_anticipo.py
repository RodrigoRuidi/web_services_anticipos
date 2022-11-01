# Web services Rol
from flask import Blueprint, request, jsonify
from models.estado_anticipo import Estado_anticipo
import json
import validar_token as vt

ws_estado_anticipo = Blueprint('ws_estado_anticipo', __name__)


@ws_estado_anticipo.route('/estado_anticipo/listar', methods=['POST'])
@vt.validar_token
def listar_motivos_anticipos():
    if request.method == 'POST':
        obj = Estado_anticipo()
        rpta_estado_anticipo = obj.listar_estados_anticipos()
        datos = json.loads(rpta_estado_anticipo)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
