# Calculadora de Hipoteca Inversa
Esta es una aplicación web desarrollada con Flask que permite calcular diferentes tipos de hipotecas inversas: temporal, vitalicia y única.
Cómo está creado
La aplicación está construida utilizando Flask, un marco web para Python. Consta de los siguientes archivos principales:

App.py: El archivo principal que inicia la aplicación Flask.
Controller.py: Contiene las rutas y las funciones que manejan las solicitudes HTTP.
Modell.py: Contiene la clase HipotecaInversaque implementa los cálculos para los diferentes tipos de hipotecas inversas.
Config.py: Almacena las credenciales de conexión a la base de datos PostgreSQL.
index.html: La página principal que muestra el formulario para ingresar los datos de la hipoteca inversa.
resultado.html: La página que muestra los resultados del cálculo de la hipoteca inversa.
styles.css: Archivo CSS que contiene los estilos para la interfaz de usuario.

Cómo hacerlo funcionar

Asegúrese de tener instalado Python y las siguientes dependencias:

Matraz
psycopg2 (para la conexión a PostgreSQL)
python-dotenv (para cargar variables de entorno desde un archivo .env)


Clona o descarga este repositorio en tu máquina local.
Configure las credenciales de conexión a la base de datos PostgreSQL en el archivo Config.py.
En la terminal, navega hasta la carpeta del proyecto y ejecuta el siguiente comando:
Copiar códigopython App.py
Esto iniciará la aplicación Flask en modo de depuración.
Abra su navegador web y visite http://localhost:5000para acceder a la aplicación.

Qué hace
La aplicación permite calcular tres tipos de hipotecas inversas:

Hipoteca Inversa Temporal : Calcula el saldo de la deuda después de un período de tiempo especificado en años.
Hipoteca Inversa Vitalicia : Calcula el saldo de la deuda considerando la esperanza de vida del prestatario.
Hipoteca Inversa Única : Calcula el saldo de la deuda final y el número de meses necesarios para que la deuda alcance el valor total de la vivienda.

Los resultados de los cálculos se almacenan en una base de datos PostgreSQL para su posterior análisis o procesamiento.
