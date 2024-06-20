nos ubicamos en la parte de Terminal de Visual studio Code

--- creacion de entorno Virtual en visual studio code 
py -m venv .\proyfinal\
-- permiso para realizar instalaciones en este entorno
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
-- luego me paso a la carpeta scripts 
 cd Scripts
-- finalmente activo el ambiente 
.\activate

y ya quedo con un ambiente valido donde puedo instalar las librerias que necesito.

intrucciones para instalar paquetes de python 

 pip
 py pip
 py -m pip
 py -m pip install pandas
 
 para instalar el archivo de requerimientos en un proyecto python con la siguiente instruccion 
 $ pip install -r requirements.txt
 
 para el proyecto de ci-cd jenkins se creo el entorno virtual
 proyciJenkins
 
 se debe lanzar desde la carpeta de SRC
  uvicorn main:app --reload
  http://127.0.0.1:8000/docs
  http://127.0.0.1:8000/sabana/
  http://127.0.0.1:8000/diplomado/
  
 
 
 instalacion de jemkims em docker 
 https://www.youtube.com/watch?v=orXmCzxtoYw
 
 Descargar la imagen 
   docker pull jenkins/jenkins
 
 instalacion de la imagen de jenkins en un contenedor de docker
 name : nombre del contenedor
 -p puerto a exponer
 -v volumen para persisitir los datos del contenedor 
 
 docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins
 
 para sacar la contraseña admin de docker 
 docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
 con docker exec ejecutamos un comando en docker 
 la contraseña admin de docker es: 9be3430d9bea44a79863c8dbdbaf6199
 
 usuario: johncamr
 pwd: Jenkins123
 email: johncamr@gmail.com
 http://localhost:8080/
 
 