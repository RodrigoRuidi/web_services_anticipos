from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder


class Informe_gasto():
    def __init__(self, id=None, num_informe=None, fecha_hora=None, estado_id=None, total_rendir=None, total_rendido=None, anticipo_id=None):
        self.id = id
        self.num_informe = num_informe
        self.fecha_hora = fecha_hora
        self.estado_id = estado_id
        self.total_rendir = total_rendir
        self.total_rendido = total_rendido
        self.anticipo_id = anticipo_id


    def listar_informes_gasto_docente(self, docente_id):
        # Abrir la conexion
        con = bd().open

        # Crear un cursor
        cursor = con.cursor()

        # Preparar la consulta SQL
        sql = "SELECT num_informe, fecha_hora, e.id AS estado_id, e.descripcion AS estado, total_rendido, a.descripcion AS anticipo, a.fecha_inicio, a.fecha_fin FROM informe_gasto inf INNER JOIN estado_anticipo e ON inf.estado_id = e.id INNER JOIN anticipo a ON inf.anticipo_id = a.id INNER JOIN usuario doc ON a.usuario_id = doc.id WHERE doc.id = %s; "

        # Ejecutar la consulta
        cursor.execute(sql, [docente_id])

        # Almacenar los datos que devuelva de la conulsta
        datos = cursor.fetchall()

        # Cerrar el cursor y la conexion
        cursor.close()
        con.close()

        # Retornar datos
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Listado informe gastos docente'}, cls=CustomJsonEncoder)

        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})

    def listar_informes_gasto_jefe_admin(self):
        # Abrir la conexion
        con = bd().open

        # Crear un cursor
        cursor = con.cursor()
        sql = "SELECT num_informe, fecha_hora, e.id AS estado_id, e.descripcion AS estado, total_rendido, a.descripcion AS anticipo, a.fecha_inicio, a.fecha_fin, CONCAT(doc.nombres, ', ', doc.apellidos) AS docente FROM informe_gasto inf INNER JOIN estado_anticipo e ON inf.estado_id = e.id INNER JOIN anticipo a ON inf.anticipo_id = a.id INNER JOIN usuario doc ON a.usuario_id = doc.id"
        cursor.execute(sql)
        # Almacenar los datos que devuelva de la conulsta
        datos = cursor.fetchall()

        # Cerrar el cursor y la conexion
        cursor.close()
        con.close()

        # Retornar datos
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Listado informes gasto'}, cls=CustomJsonEncoder)

        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})
