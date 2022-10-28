from conexionBD import Conexion as bd
import json
from util import CustomJsonEncoder

class Rol():
    def __innit__(self, id=None,nombre=None,estado=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    def listar_roles(self):
        con = bd().open
        cursor = con.cursor()
        sql = "SELECT * FROM rol WHERE estado = '1'"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        con.close()

        #Return data
        if (datos):
            return json.dumps({'status':True,'data':datos,'message':'Lista de roles'}, cls= CustomJsonEncoder)
        else :
            return json.dumps({'status': False, 'data':'','message': 'No hay datos para mostrar'})
