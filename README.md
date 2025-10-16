# test_ridery_car
A test tecnical
Pasos a seguir para poder ejecutar el 
1. Clonar repositorio 
2. abrir la terminal de su preferencia bash zsh 
3. ubicarse en la raiz del repositorio
3.1 arreglar el nombre de env.txt a .env y luego colocar los datos correspondientes a su equipo local, host, port, y nombre de la bd que creo en odoo, usuario admin y clave admin
4.1  Ejecucion semiautomatica
    1. darle permisos al script init_setup.bash con el comando sudo chmod +x init_setup.bash
    2. Ejecutar el sistema con el comando ./init_setup.bash 
4.2 ejecucion manual
    <!-- Levantar odoo -->
    1.ejecutar el comando "cd odoo"
    2. ejecutar el comando "docker compose up"
    <!-- Levantar node -->
    3. abrir otra pestaña y ejecutar el comando "cd ../node"
    4. ejecutar el comando node server.js 
5. entrar en la url http://localhost:8069
6. aqui le aparecera una vista donde tendra que llenar los campos necesarios para crear la bd 
7. master password(Clave de la base de datos) colocar clave de su preferencia
   email(usuario administrador) por costumbre se coloca admin
   password(clave del administrador) a su preferencia como llenar
   language(lenguaje del idioma) 
   country(pais de residencia)
8. darle al boton continue o createdb
9. En su esquina superior izquierda  le aparecera el menu home al darle click se le desplegara dos opciones darle en la de aplicaciones instalar el modulo vehicles_logs  automaticamente se instalara el modulo vehicle y contactos


