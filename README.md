# APP-QR #

La idea final de la aplicacion seria que cuando te llega la cuenta, ejemplo, en un restaurante, y al momento de pagar, las personas involucradas quieren pagar todos con la billetera virtual mas famosa, es un chino, ya que cuando escaneas el QR te pone el monto total a pagar. Entonces, en este caso, cuando vos escanees el codigo QR, te va a pedir la cantidad de personas que son en total, que ingreses los mails de sus cuentas de mercadopago, y el monto total de la cuenta. Esto lo que va a realizar, es enviarte una notificacion a tu cuenta, con el monto a pagar. A su vez, en caso de que no llegue la notificacion, tambien va a crear un QR para cada usuario, donde lo van a poder escanear y van a ser dirigidos al pago.

NOTAS: Como veran, tambien corre un postgres, la idea de esto es dejar un registro de todas las transacciones.
NOTAS: La app esta muy verde todavia, pero la idea es ir mejorandola con el tiempo y que el repositorio siga creciendo.


# DESAFIO M14 #

Para poder probar la aplicacion, lo primero que vamos a tener que hacer es clonarnos el Repositorio. Para ello, dentro de la terminal de Visual Studio Code, vamos a ejecutar el siguiente comando:

- git clone https://github.com/martinlopez5/desafio-M14.git


Una vez que tenemos el Repositorio clonado en nuestro local, vamos a dirigirnos al directorio 'App-QR', donde se encuentra todo lo necesario para que la App funcione.

- cd App-QR
![Alt text](Images/image1.png)


Dentro del directorio App-QR, vamos a ver que hay un Script 'run.sh', el cual al ejecutarlo crea la imagen, el contenedor y sube la imagen a DockerHub. Para correrlo, vamos a tener que ejecutar el siguiente comando:

- sh run.sh
![Alt text](Images/image2.png)

Aca podemos ver el proceso del script:
![Alt text](Images/image3.png)




Una vez terminado, vas a ingresar a la siguiente direccion en el navegador que desees http://localhost:5000 y se va a poder ver el funcionamiento de la misma.

![Alt text](Images/image4.png)


Tambien podemos ingresar a nuestra cuenta de DockerHub y revisar que la imagen se haya subido correctamente.
![Alt text](Images/image5.png)







# DESAFIO M15 #

## JENKINS ##

Para este Desafio, lo podemos realizar de 2 formas. La opcion Nº1 es si estamos trabajando desde Windows, y la opcion Nº2 es si estamos trabajando desde Linux. (Aunque tambien se puede usar el Nº1 desde Linux). En este caso, utilice la opcion Nº2 ya que trabajo desde Linux.

Lo primero que vamos a realizar es la instalacion de Jenkins, para ello vamos a ejecutar el siguiente comando:

- docker run -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home --restart=on-failure jenkins/jenkins:lts
![Alt text](Images/image.png)


Una vez que corrimos dicho comando, vamos a correr el siguiente comando, para revisar que nuestro contenedor de Jenkins este funcionando:

- docker ps
![Alt text](Images/image6.png)


Como podemos ver, esta corriendo ok, con lo cual ahora vamos a proceder a instalar Jenkins dentro de nuestro contenedor, para ello vamos a ejecutar el siguiente comando:

- docker exec -it --user root <container id> bash
![Alt text](Images/image7.png)


Una vez dentro de nuestro contenedor, vamos a ejecutar el siguiente comando, para realizar la instalacion de Docker:

- curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall


Cuando la instalacion haya finalizado, vamos a escribir 'exit', para salir de nuestro contenedor y vamos a ejecutar el siguiente comando en nuestra terminal:

- sudo chmod 666 /var/run/docker.sock


De esta forma, ya vamos a tener funcionando Docker en nuestro conteneder, ahora vamos a proceder a ingresar a Jenkins, para ello abrimos el navegador de nuestra preferencia, e ingresamos a la siguiente URL:

- http://localhost:8080

![Alt text](Images/image8.png)

Aca nos va a pedir que ingresemos la InitialPassword, para ello volvemos a nuestra consola y ejecutamos el siguiente comando:

- docker exec -it sharp_snyder cat /var/jenkins_home/secrets/initialAdminPassword

Pegamos la Password que nos aparece en pantalla y clickeamos en Continue. La proxima pantalla nos va a pedir que creemos nuestro usuario y password.
![Alt text](Images/image9.png)

Luego nos va a pedir que instalemos los Plugins, en este caso seleccionamos la opcion 'Install Suggested Plugins'
![Alt text](Images/image10.png)

Una vez que haya finalizado la instalacion de los Plugins, ya vamos a estar dentro de Jenkins. Para poder crear nuestro Pipeline vamos a hacer click en la opcion 'New Task'.

![Alt text](Images/image11.png)

Vamos a ingresar el nombre de nuestro Pipeline y seleccion la opcion 'Multibranch Pipeline' y le damos a Continue.
![Alt text](Images/image12.png)

En la parte de 'Branch Sources', vamos a ingresar la URL de este repositorio.
![Alt text](Images/image13.png)

Bajamos un poco mas, y en la parte de 'Build Configuration', vamos a escribir la ruta de nuestro Jenkinsfile, que en este caso es Jenkins/Jenkinsfile. Y como ultimo paso, hacemos click en Apply y luego a Save.
![Alt text](Images/image14.png)



Antes de correr el Pipeline, tenemos que cargar nuestras credenciales de DockerHub, para que pueda subir la imagen. Para ello, vamos al inicio de Jenkins e ingresamos a la opcion 'Administrar Jenkins'.
![Alt text](Images/image15.png)

Luego vamos a la opcion 'Credentials'.
![Alt text](Images/image16.png)

Ingresamos en 'System'.

![Alt text](Images/image17.png)

Ahora ingresamos en 'Global Credentials'.
![Alt text](Images/image18.png)

Clickeamos en 'Add Credentials'.
![Alt text](Images/image19.png)

Cargamos nuestras credenciales.
![Alt text](Images/image20.png)



Ahora si, ingresamos a nuestro Pipeline.
![Alt text](Images/image21.png)

Una vez dentro, vamos a ver que esta creado uno con el nombre de nuestra rama, en este caso 'main', y le damos al simbolo de play, para correr el mismo.
![Alt text](Images/image22.png)

Vamos a ver que empieza a correr.

![Alt text](Images/image23.png)

Ingresamos al mismo, y vamos a poder ver el paso a paso.
![Alt text](Images/image24.png)

Ingresamos al ultimo, que en este caso es el #6. Y vamos a la opcion de 'Console Output', donde vamos a poder ver todo el proceso.
![Alt text](Images/image25.png)

Y como paso final, vamos a ingresar a nuestra cuenta de DockerHub, para ver si pusheo la imagen correctamente. La cual tendria que tener el Tag 6.0.
![Alt text](Images/image26.png)



## GITHUB ACTIONS ##

Para poder realizar esta parte del Desafio, lo primero que vamos a hacer es clonarnos nuestro repositorio en nuestra PC local, con el siguiente comando:

- git clone https://github.com/mi-repositorio/

Una vez que lo tengamos clonado, vamos a crear una carpeta con el siguiente comando:

- mkdir -p .github/workflows

Dentro de esta carpeta, vamos a agregar nuestro archivo yml, en el cual se van a definir los pasos que querramos ejecutar. (podemos ponerle el nombre que deseemos)

- touch pipeline.yml

Dentro de este archivo, vamos a delcarar los pasos que queremos realizar. En este caso sacamos de la pagina de Marketplace de Github, 2 Actions. Build and Push / Hadolint.
![Alt text](Images/image27.png)

Para que esto funcione, vamos a tener que cargar las Secrets en nuestro repositorio, para ello vamos a 'Settings'.
![Alt text](Images/image28.png)

Dentro de 'Settings', vamos a 'Actions', que se encuentra dentro de 'Secrets and variables'.
![Alt text](Images/image29.png)

Dentro de 'Actions', vamos a crear nuestras 2 secrets.
![Alt text](Images/image30.png)


Una vez que tenemos las credenciales cargadas, vamos a ejecutar los siguientes comandos para realizar un push a nuestro repositorio.

- git add .

- git commit -m "Update pipeline.yml"

- git push

Ahora, cualquier cambio que realicemos dentro de la carpeta con nuestro codigo, se va a ejecutar el pipeline.yml, en este caso, todo cambio que realice sobre la carpeta App-QR, va a activar el pipeline.yml.

Aca podemos ver que se ejecuto correctamente el Hadolint y el Build and Push.
![Alt text](Images/image31.png)

Tambien si ingresamos a nuestra cuenta de DockerHub, vamos a ver el Push de nuestra imagen creada.
![Alt text](Images/image32.png)







# DESAFIO M16 - M17 #

## VAGRANT ##

Dentro de la carpeta Vagrant, van a encontrar los archivos Vagrantfile y provision.sh, los cuales tienen todo lo necesario para poder trabajar desde el Desafio M14, hasta el Desafio M16-M17.
Nos clonamos el repo, nos posicionamos sobre la carpeta Vagrant y con el siguiente comando, vamos a poder levantar la maquina virtual:

- vagrant up

Una vez levantada, nos conectaremos con el comando:

- vagrant ssh



## DOCKER ##

La maquina de vagrant viene con todo lo necesario para correr Dockerizar aplicaciones. Y dentro del repositorio, si nos posicionamos en la carpeta App-QR, vamos a tener el DockerFile y DockerCompose de la aplicacion y un scritp 'run.sh' el cual buildea la aplicacion de forma local y sube la imagen al repositorio de DockerHub que se le indique.

![Alt text](Images/image33.png)



## AUTOMATIZACION DE DOCKERFILE"

En este caso, utilizamos GitHub Action para automatizar el build, push y test de la aplicacion. En este caso, cada vez que se haga un cambio dentro de la carpeta App-QR y se realice el push al repositorio, esto activara las Actions, las cuales correran un Test para el Dockerfile (Hadolint), luego realizara el Build de la aplicacion, una vez finalizado el build, va a ejecutar un Test de Python y si todo esta ok, va a proceder a subir la imagen a DockerHub.

![Alt text](Images/image34.png)



## KUBERNETES ##


Saludos.
