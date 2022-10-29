# Web services Rol
from flask import Blueprint, request, jsonify
from models.rubro import Rubro
import json
import validar_token as vt

ws_rubro = Blueprint('ws_rubro', __name__)


@ws_rubro.route('/rubro/listar', methods=['POST'])
@vt.validar_token
def listar_rubros():
    if request.method == 'POST':
        obj = Rubro()
        rpta_rubros = obj.listar_rubros()
        datos = json.loads(rpta_rubros)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
