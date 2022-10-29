# Web services Rol
from flask import Blueprint, request, jsonify
from models.motivo_anticipo import Motivo_anticipo
import json
import validar_token as vt

ws_motivo_anticipo = Blueprint('ws_motivo_anticipo', __name__)


@ws_motivo_anticipo.route('/motivo_anticipo/listar', methods=['POST'])
@vt.validar_token
def listar_motivos_anticipos():
    if request.method == 'POST':
        obj = Motivo_anticipo()
        rpta_motivos_anticipos = obj.listar_motivos_anticipos()
        datos = json.loads(rpta_motivos_anticipos)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
