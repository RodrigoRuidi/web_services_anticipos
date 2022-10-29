from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder


class Tipo_comprobante():
    def __innit__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def listar_tipo_comprobante(self):
        con = bd().open
        cursor = con.cursor()
        sql = "SELECT * FROM tipo_comprobante ORDER BY nombre"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        con.close()

        #Return data
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de tipos de comprobantes'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})
