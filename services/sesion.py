#Web services login
from flask import Blueprint,request,jsonify
from models.sesion import Sesion
from config import SecretKey
import jwt
import datetime
import json

#Interface for web services managment
ws_sesion = Blueprint('ws_sesion',__name__)

@ws_sesion.route('/login',methods=['POST'])

def login():
    if (request.method == 'POST'):
      #Write data by POST
      email = request.form['email']
      password = request.form['password']

      #Instance a sesion object
      obj_sesion = Sesion(email,password)
      #Execute login method
      rpta_inicio_sesion = obj_sesion.iniciar_sesion()
      #Convert the response in JSON String to JSON Object String
      datos_sesion_JSON = json.loads(rpta_inicio_sesion)

      if datos_sesion_JSON['status'] == True:
        #Save user id in the token
        user_id = datos_sesion_JSON['data']['id']
        #Generate token
        token = jwt.encode({'user_id':user_id,'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=60)},SecretKey.JWT_SECRET_JEY)

        #Include token in the response
        datos_sesion_JSON['data']['token'] = token

        #Update generated token in database
        obj_sesion.actualizar_token(token,user_id)

        #Show web services response
        return jsonify(datos_sesion_JSON), 200 #OK
      else:
        return jsonify(datos_sesion_JSON), 401  # Not Authorized
