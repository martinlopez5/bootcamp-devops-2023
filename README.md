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

![Alt text](Images/image.png)

Saludos.
