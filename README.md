## APP-QR ##

La idea final de la aplicacion seria que cuando te llega la cuenta por dar un ejemplo en un restaurante, y al momento de pagar, los comensales quieren pagar todos con mercadopago, es un chino, ya que cuando escaneas el QR te pone el monto total a pagar. Entonces, en este caso, cuando vos escanees el codigo QR, te va a llevar a una pagina, donde te va a pedir la cantidad de personas que son en total, que ingreses los mails de sus cuentas de mercadopago, le vas a dar enviar y a cada uno le va a llegar una notificacion a su mercagopago con el monto a pagar, y asi para cada uno de los usuarios. Una vez que pagaron todos, automaticamente al que escaneo el QR, le sale como que el monto fue pagado en su totalidad. Ademas, genera un QR para cada uno de los usuarios, por si por algun motivo no llego la notificacion, entonces escaneando el QR, lo va a llevar directo a mercadopago para que realice el pago.

NOTAS: Como veran, tambien corre un postgres, la idea de esto es dejar un registro de todas las transacciones, por el momento corre en el mismo contenedor, pero mi idea a futuro es que corran en distintos contenedores.

Todavia es una version BETA, tengo varias cosas para seguir mejorando, que espero poder hacerlo en los proximos desafios.


## DESAFIO M14 ##

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







## DESAFIO M15 ##

# JENKINS #

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



# GITHUB ACTIONS #









![Alt text](Images/image.png)

Saludos.
