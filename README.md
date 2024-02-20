## Project Red Code
Python (Dash) + Gunicorn on Docker Compose. 

Alvaro Velasco Prieto

## DOCS
Documentacion pendiente

## Requisitos

Se trata de una aplicación web para la cual necesitará un navegador instalado.
Si no dispone de ello, para instalar Google Chrome emplearemos los siguientes comandos:
Primero actualizamos el sistema:
```bash
$ sudo apt-get update
```

Descargamos el paquete para la instalación de chrome:
```bash
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Instalamos el paquete:
```bash
$ sudo apt install ./google-chrome-stable_current_amd64.deb
```


Para hacer el despliegue de la página usaremos Docker, si no dispone de docker en su sistema instalelo mediante los siguientes comandos:
Primero actualizamos el sistema:
```bash
$ sudo apt-get update
```
E instalamos docker:
```bash
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Además, instalamos docker-compose:
```bash
$ sudo apt install docker-compose
```

## Instrucciones de uso

Para obtener los archivos del directorio del proyecto se ha de emplear el siguiente comando:
```bash
$git clone https://github.com/AlvaroVelascoPrieto/ProjectRedCode
```

Una vez obtenidos los archivos del repositorio, accedemos a la carpeta y construimos la imagen web mediante el siguiente comando:
#Modo development:
```bash
$ sudo docker build -f app/Dockerfile.dev -t app . 
```
Modo deployment
```bash

$ sudo docker build -f app/Dockerfile -t app . 
```
```bash

$ sudo docker build -f recepcion/Dockerfile -t app2 . 
```


Tras esto, desplegamos los servicios mediante:
```bash
$ sudo docker compose up 
```

Una vez hecho esto la aplicación web estará corriendo en el puerto 8050. (http://localhost:8050/).

