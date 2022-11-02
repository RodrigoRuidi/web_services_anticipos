# Web services Tarifa
from flask import Blueprint, request, jsonify
from models.informe_gasto import Informe_gasto
import json
import validar_token as vt

ws_informe_gasto = Blueprint('ws_informe_gasto', __name__)


@ws_informe_gasto.route('/informe_gasto/docente/listar', methods=['POST'])
@vt.validar_token
def listar_informe_gasto_docente():
    if request.method == 'POST':
        if not 'docente_id' in request.form:
          return jsonify({'status': False, 'data': '', 'message': 'Falta docente'}), 403
        else:
            docente_id = request.form['docente_id']
            obj = Informe_gasto()
            rpta_informe_gasto_docente = obj.listar_informes_gasto_docente(docente_id)
            datos = json.loads(rpta_informe_gasto_docente)
            return jsonify(datos), 200
    else:
        return jsonify(datos), 401


@ws_informe_gasto.route('/informe_gasto/administracion/listar', methods=['POST'])
@vt.validar_token
def listar_informe_gasto_jefe_admin():
    if request.method == 'POST':
        obj = Informe_gasto()
        rpta_informe_gasto_admin = obj.listar_informes_gasto_jefe_admin()
        datos = json.loads(rpta_informe_gasto_admin)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
