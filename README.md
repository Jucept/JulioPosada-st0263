# JulioPosada-st0263
## Información de la materia: ST0263 - Tópicos Especiales en Telemática

## Estudiante: Julio César Posada Torres
- Correo electrónico: jcposadat@eafit.edu.co

## Profesor: Alvaro Enrique Ospina Sanjuan
- Correo electrónico: aeopsinas@eafit.edu.co

# P2P - Comunicación entre procesos mediante API REST, RPC y MOM, Reto No 1 y 2

# 1. breve descripción de la actividad
#
La actividad consistió en diseñar e implementar un sistema P2P (peer-to-peer) que permitiera la comunicación entre procesos utilizando API REST, RPC y MOM (Message-Oriented Middleware). El sistema debía ser capaz de compartir archivos de manera distribuida y descentralizada entre los nodos de la red P2P.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Se implementó un servidor gRPC para manejar diferentes tipos de llamadas RPC, como unary, server-side streaming, client-side streaming y bidirectional streaming.
- Se diseñó la estructura del sistema P2P, incluyendo la comunicación entre los nodos.
- Se utilizaron librerías estándar de Python, como concurrent.futures y threading, para garantizar la concurrencia en los microservicios del servidor.
- Se realizaron pruebas y se desarrolló en localhost.


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- No se implementó la lógica de negocio para compartir y consultar archivos entre los nodos de la red P2P.
- No se realizó depliegue en AWS.
- Un aspecto a mejorar es cambiar los métodos de pruebas de mensajes para poder usar archivos reales.
- No se usó API REST


# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
## Esquema de la arquitectura del modelo gRPC que se uso para el desarrollo del reto
![image](https://github.com/Jucept/JulioPosada-st0263/assets/82523496/0085102b-71c6-4b92-b5b1-a3cef9999ecd)


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
Se necesita tener instaladas las herramientas para desarrollo con grpc.
> pip install grpcio-tools
Se deberan ejecutar dos terminales las cuales ubicara en la carpeta donde se encuentra ubicado el proyecto.
A continuación se deberan ejecutar los archivos "server.py" y "client.py".
![image](https://github.com/Jucept/JulioPosada-st0263/assets/82523496/2e7440f2-29f6-4fc0-8567-1b597503d8b2)
Mientras que el servidor espera a alguna petición por medio de RPC al cliente se le muestra por pantalla las cuatro opciones de métodos RPC que se pueden realizar, el cliente decide cuál usar.


## detalles del desarrollo.
**server.py:** Contiene la implementación del servidor gRPC. Maneja varios tipos de llamadas RPC, como unary, server-side streaming, client-side streaming y bidirectional streaming.
**client.py:** Contiene la implementación del cliente para interactuar con el servidor. Llama a los diferentes métodos RPC ofrecidos por el servidor.
**hello.proto:** La definición del servicio y los mensajes del protocolo gRPC. Por medio del siguiente comando se generan 2 archivos más.
> python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/hello.proto
**hello_pb2.py:** Archivo generado que contiene las clases de mensajes para gRPC.
**hello_pb2_grpc.py:** Archivo generado que contiene las clases de servicio para gRPC.

## detalles técnicos
## Configuración de puertos:
### Dentro de server.py:
_server.add_insecure_port("localhost:50051"):_ Aquí se configura el puerto en el que el servidor escuchará las solicitudes entrantes. 
### Dentro de client.py:
_with grpc.insecure_channel('localhost:50051') as channel:_ Aquí se especifica la dirección IP y el puerto del servidor al que el cliente se conectará.

## Pantallazos 
### Configuración de puertos:
![image](https://github.com/Jucept/JulioPosada-st0263/assets/82523496/450b2bc9-8625-4213-a1a2-bc5ad57fecf8)
### Organización del código:
![image](https://github.com/Jucept/JulioPosada-st0263/assets/82523496/3573ad9e-cbe6-44f9-bafe-c34493ae00d0)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
**Lenguaje de Programación:** Python 🐍
## Librerías y Paquetes:
**grpcio:** Implementa el framework gRPC para Python.
**protobuf:** Proporciona soporte para la serialización y deserialización de mensajes en gRPC.
**concurrent.futures:** Utilizado para manejar la concurrencia en el servidor.
**time:** Para el manejo del tiempo y las pausas en la ejecución del código.
**futures:** Proporciona una interfaz para trabajar con futuros y procesos concurrentes en Python.

# referencias:
## [sitio1-url](https://www.geeksforgeeks.org/what-is-p2p-peer-to-peer-process/) 
## [sitio2-url](https://www.youtube.com/watch?v=gnchfOojMk4&pp=ygUEZ3JwYw%3D%3D)
## [sitio3](https://www.youtube.com/watch?v=WB37L7PjI5k&t=838s&pp=ugMICgJlcxABGAHKBQtncnBjIHNlcnZlcg%3D%3D)}
