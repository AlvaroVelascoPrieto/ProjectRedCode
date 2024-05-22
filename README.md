# FSB 2024 - Remote Data Analisys and Aquisition (Telemetry)
Python (Dash) + Redis + Gunicorn on Docker Compose. 

Alvaro Velasco Prieto

## DOCS
Documentation in progress... (Available 31/07/2024)

## Deployment
In order to deploy this web app you will use Docker & Docker Compose. To install these tools type the following commands:
Update your system:
```bash
$ sudo apt-get update
```
Install Docker:
```bash
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Install docker-compose:
```bash
$ sudo apt install docker-compose
```

To obtain all files in the directory use the following command:
```bash
$ git clone https://github.com/AlvaroVelascoPrieto/ProjectRedCode
```

Once you have downloaded the files from the repository, access the folder and build the web image with the following command:

Development mode:

```bash
$ sudo docker build -f app/Dockerfile.dev -t app . 
```
Deployment mode
```bash

$ sudo docker build -f app/Dockerfile -t app . 
```

Now build the data aquisition image:
```bash

$ sudo docker build -f recepcion/Dockerfile -t app2 . 
```


After building the images you can deploy all the services using docker-compose:
```bash
$ sudo docker compose up 
```

Once this process is complete the app wil be running locally on port 8050. (http://localhost:8050/).

