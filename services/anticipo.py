# Web services Tarifa
from flask import Blueprint, request, jsonify
from models.anticipo import Anticipo
import json
import validar_token as vt

ws_anticipo = Blueprint('ws_anticipo', __name__)


@ws_anticipo.route('/anticipos/docente/listar', methods=['POST'])
@vt.validar_token
def listar_anticipos_docente():
    if request.method == 'POST':
        if not 'docente_id' in request.form:
          return jsonify({'status': False, 'data': '', 'message': 'Falta docente'}), 403
        else :
            docente_id = request.form['docente_id']
            obj = Anticipo()
            rpta_anticipos_docente = obj.listar_anticipos_docente(docente_id)
            datos = json.loads(rpta_anticipos_docente)
            return jsonify(datos), 200
    else:
        return jsonify(datos), 401


@ws_anticipo.route('/anticipos/admin/listar', methods=['POST'])
@vt.validar_token
def listar_anticipos_admin():
    if request.method == 'POST':
          if not 'estado_anticipo_id' in request.form:
              obj = Anticipo()
              rpta_anticipos_admin = obj.listar_anticipos_admin()
              datos = json.loads(rpta_anticipos_admin)
              return jsonify(datos), 200
          else :
            estado_anticipo_id = request.form['estado_anticipo_id']
            obj = Anticipo()
            rpta_anticipos_admin = obj.listar_anticipos_admin(estado_anticipo_id)
            datos = json.loads(rpta_anticipos_admin)
            return jsonify(datos), 200
    else:
        return jsonify(datos), 401
