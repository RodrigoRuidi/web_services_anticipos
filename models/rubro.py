from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder


class Rubro():
    def __innit__(self, id=None, nombre=None,se_calcula_por_dia=None):
        self.id = id
        self.nombre = nombre
        self.se_calcula_por_dia = se_calcula_por_dia

    def listar_rubros(self):
        con = bd().open
        cursor = con.cursor()
        sql = "SELECT * FROM rubro ORDER BY nombre"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        con.close()

        #Return data
        if (datos):
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de rubros'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': '', 'message': 'No hay datos para mostrar'})
