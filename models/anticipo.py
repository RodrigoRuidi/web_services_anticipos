from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder


class Anticipo():
    def __init__(self, id=None, descripcion=None, fecha_inicio=None, fecha_fin=None, monto_total=None, estado_anticipo_id=None, motivo_anticipo_id=None, sede_id=None, usuario_id=None):
        self.id = id
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.monto_total = monto_total
        self.estado_anticipo_id = estado_anticipo_id
        self.motivo_anticipo_id = motivo_anticipo_id
        self.sede_id = sede_id
        self.usuario_id = usuario_id

    def listar_anticipos_docente(self, docente_id):
        # Abrir la conexion
        con = bd().open

        # Crear un cursor
        cursor = con.cursor()

        # Preparar la consulta SQL
        sql = "SELECT an.descripcion, an.fecha_inicio, an.fecha_fin, an.monto_total, es.descripcion AS estado FROM anticipo AS an INNER JOIN estado_anticipo AS es on (es.id = an.estado_anticipo_id) WHERE an.usuario_id=%s"

        # Ejecutar la consulta
        cursor.execute(sql, [docente_id])

        # Almacenar los datos que devuelva de la conulsta
        datos = cursor.fetchall()

        # Cerrar el cursor y la conexion
        cursor.close()
        con.close()

        # Retornar datos
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Listado anticipos docente'}, cls=CustomJsonEncoder)

        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})

    def listar_anticipos_admin(self, estado_id=0):
            # Abrir la conexion
            con = bd().open

            # Crear un cursor
            cursor = con.cursor()
            if estado_id == 0 :
                sql = "SELECT an.descripcion, an.fecha_inicio, an.fecha_fin, an.monto_total, es.descripcion AS estado FROM anticipo AS an INNER JOIN estado_anticipo AS es on (es.id = an.estado_anticipo_id)"
                cursor.execute(sql)

            else :
              sql = "SELECT an.descripcion, an.fecha_inicio, an.fecha_fin, an.monto_total, es.descripcion AS estado FROM anticipo AS an INNER JOIN estado_anticipo AS es on (es.id = an.estado_anticipo_id) WHERE an.estado_anticipo_id=%s"
              cursor.execute(sql, [estado_id])

            # Almacenar los datos que devuelva de la conulsta
            datos = cursor.fetchall()

            # Cerrar el cursor y la conexion
            cursor.close()
            con.close()

            # Retornar datos
            if (datos):
                return json.dumps({'status': True, 'data': datos, 'message': 'Listado anticipos admin'}, cls=CustomJsonEncoder)

            else:
                return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})
