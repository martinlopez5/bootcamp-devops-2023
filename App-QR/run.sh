#!/bin/bash

#Run Docker Compose
docker-compose up --build -d

# Obtener la lista de imágenes de Docker
image_list=$(docker images --format "{{.Repository}}:{{.Tag}}")

# Mostrar las imágenes disponibles al usuario
echo "Imágenes de Docker disponibles:"
echo "$image_list"

# Solicitar al usuario que seleccione una imagen
read -p "Seleccione la imagen que desea subir a Docker Hub: " selected_image

# Verificar si la imagen seleccionada existe
if echo "$image_list" | grep -q "$selected_image"; then
    # Solicitar credenciales de Docker Hub
    read -p "Ingrese su nombre de usuario de Docker Hub: " username
    read -s -p "Ingrese su contraseña de Docker Hub: " password
    echo

    # Iniciar sesión en Docker Hub
    docker login --username "$username" --password "$password"

    # Etiquetar la imagen seleccionada para Docker Hub
    docker tag "$selected_image" "$username/$selected_image"

    # Subir la imagen etiquetada a Docker Hub
    docker push "$username/$selected_image"

    # Cerrar sesión en Docker Hub
    docker logout

    echo "La imagen ha sido subida exitosamente a Docker Hub."
else
    echo "La imagen seleccionada no existe. ¡Adiós!"
fi



#Borrar imagen y contendor
# while true; do
    # read -p "Do you wish to delete the container and image? yes/no: " yn
    # case $yn in
        # [Yy]* ) docker stop $CONTAINERIMAGE; docker rm $CONTAINERIMAGE; docker rmi $IMAGENAME; exit;;
        # [Nn]* ) exit;;
        # * ) echo "Please answer yes or no.";;
    # esac
# done