“compliance-api” es una API REST desarrollada en Python3.7 utilizando el microframework Flask. 

Publica dos métodos:

- POST ../api/v1/compliance/systeminfo: Por medio del cual espera recibir una firma en formato .json, con información del host en el que se ejecute “compliance-agent” y genera un archivo .json.

Formato de firma:

{
   "processor":"Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz",
   "operative_system":{
      "name":"Linux debian",
      "version":"#1 SMP Debian 4.19.160-2 (2020-11-28)"
   },
   "server_ip":"10.0.2.15",
   "active_processes":[
      {
         "pid":1,
         "cpu_percent":0.0,
         "name":"systemd"
      },
      {
         "pid":2,
         "cpu_percent":0.0,
         "name":"kthreadd"
      }
   ],
   "active_users":[
      {
         "name":"malasia"
      }
   ]
}


El archivo se guarda en la carpeta static/ del repositorio, nombrado con el formato:

direccion_ip_host_YYYY_MM_DD_H_M_S.json

NOTA: Se incluyó la hora en el nombre del archivo, de otro modo, se sobreescribiría si fuese generado dentro del mismo día.

 
- GET ../api/v1/compliance/systeminfo/{IP_ADDRESS + YYYY_MM_DD_H_M_S}: Por medio del cual es posible recuperar la información que envió el agente, para el host en el cual se ejecutó.

Dentro de los datos almacenados, es posible encontrar:

●      Información sobre el procesador.

●      Nombre del sistema operativo.

●      Versión del sistema operativo.

●      Listado de procesos corriendo.

●      Usuarios con una sesión abierta en el sistema.

●      IP del host en el que se ejecuta.  

Para correrla es necesario:
·         Tener instalado Python3 y Flask.
·         Inicializar la aplicación “compliance-api”:

FLASK_APP = app.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder /home/malasia/Repositorios/compliance-api
/home/malasia/Repositorios/compliance-api/venv/bin/python -m flask run

NOTA: En la carpeta venv se subieron las librerías necesarias para poder ejecutar “compliance-api”.

Dockerizacion de compliance api

-Generar imagen del contanedor

sudo docker build -t compliance-api:latest .

-Correr el contenedor de docker

sudo docker run -d --name api -p 5000:5000 compliance-api

-se expone el host 0.0.0.0:5000 para accederlo desde el host anfitrion

  http://0.0.0.0:5000/api/v1/compliance/system_info
  






