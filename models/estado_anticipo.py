from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder


class Estado_anticipo():
    def __innit__(self, id=None, descripcion=None):
        self.id = id
        self.descripcion = descripcion

    def listar_estados_anticipos(self):
        con = bd().open
        cursor = con.cursor()
        sql = "SELECT * FROM estado_anticipo ORDER BY descripcion"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        con.close()

        #Return data
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de estados anticipo'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})
