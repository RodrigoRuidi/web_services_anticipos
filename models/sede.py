from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder

class Sede():
    def __innit__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def listar_sedes(self):
        con = bd().open
        cursor = con.cursor()
        sql = "SELECT * FROM sede"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        con.close()

        #Return data
        if (datos):
            return json.dumps({'status':True,'data':datos,'message':'Lista de sedes'}, cls= CustomJsonEncoder)
        else :
            return json.dumps({'status': False, 'data':'','message': 'No hay datos para mostrar'})
