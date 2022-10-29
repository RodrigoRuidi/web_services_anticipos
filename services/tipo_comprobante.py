# Web services Rol
from flask import Blueprint, request, jsonify
from models.tipo_comprobante import Tipo_comprobante
import json
import validar_token as vt

ws_tipo_comprobante = Blueprint('ws_tipo_comprobante', __name__)


@ws_tipo_comprobante.route('/tipo_comprobante/listar', methods=['POST'])
@vt.validar_token
def listar_tipo_comprobantes():
    if request.method == 'POST':
        obj = Tipo_comprobante()
        rpta_tipo_comprobantes = obj.listar_tipo_comprobante()
        datos = json.loads(rpta_tipo_comprobantes)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
