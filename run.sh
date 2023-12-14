#!/bin/bash

#Run Docker Compose
docker-compose up --build

#Listar imagenes creadas
docker images -a

echo "Ingrese el nombre de la imagen que desea subir a DockerHub: "
read IMAGENAME

#Docker login
echo "Ahora vamos a proceder a subir nuestra imagen a Docker Hub, para ello: "
echo "Ingrese su usuario: "
read USER
echo "Ingrese su contraseña: "
read PWD
docker login -u $USER -p $PWD docker.io
#Tagear la imagen
docker tag $IMAGENAME $USER/$IMAGENAME
#Push en el registry
docker push $USER/$IMAGENAME


#Borrar imagen y contendor
# while true; do
    # read -p "Do you wish to delete the container and image? yes/no: " yn
    # case $yn in
        # [Yy]* ) docker stop $CONTAINERIMAGE; docker rm $CONTAINERIMAGE; docker rmi $IMAGENAME; exit;;
        # [Nn]* ) exit;;
        # * ) echo "Please answer yes or no.";;
    # esac
# done