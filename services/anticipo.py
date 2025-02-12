# Web services Tarifa
from flask import Blueprint, request, jsonify
from models.anticipo import Anticipo
import json
import validar_token as vt

ws_anticipo = Blueprint('ws_anticipo', __name__)

@ws_anticipo.route('/anticipo/registrar', methods=['POST'])
@vt.validar_token #f
def registrar_anticipo():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        motivo_anticipo_id = request.form['motivo_anticipo_id']
        sede_id = request.form['sede_id']
        usuario_id = request.form['docente_id']

        obj_anticipo = Anticipo(descripcion,fecha_inicio,fecha_fin,motivo_anticipo_id,sede_id,usuario_id)
        rpta_JSON = obj_anticipo.registrar()
        datos_anticipo = json.loads(rpta_JSON)

        if datos_anticipo['status']:
            return jsonify(datos_anticipo), 201 #CREATED
        else:
            return jsonify(datos_anticipo), 500 #INTERNAL SERVER ERROR


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


@ws_anticipo.route('/anticipos/jefe/listar', methods=['POST'])
@vt.validar_token
def listar_anticipos_jefe():
    if request.method == 'POST':
          if not 'estado_anticipo_id' in request.form:
              obj = Anticipo()
              rpta_anticipos_jefe = obj.listar_anticipos_jefe()
              datos = json.loads(rpta_anticipos_jefe)
              return jsonify(datos), 200
          else :
            estado_anticipo_id = request.form['estado_anticipo_id']
            obj = Anticipo()
            rpta_anticipos_jefe = obj.listar_anticipos_jefe(estado_anticipo_id)
            datos = json.loads(rpta_anticipos_jefe)
            return jsonify(datos), 200
    else:
        return jsonify(datos), 401


@ws_anticipo.route('/anticipos/admin/listar', methods=['POST'])
@vt.validar_token
def listar_anticipos_admin():
    if request.method == 'POST':
        obj = Anticipo()
        rpta_anticipos_admin = obj.listar_anticipos_admin()
        datos = json.loads(rpta_anticipos_admin)
        return jsonify(datos), 200
    else:
        return jsonify(datos), 401
