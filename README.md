# clean1 
 
 
El propósito del repositorio es explicar la introducción a GitHub, y desarrollo básico con Python 
 
 
## Comandos git 
1. Clonar un repositorio 
> Identificar el link del repositorio 
 
 
[!alt text]() 
 
 
> Sintaxis común es: https://github.com/tu_usuario/tu_repositorio.git 
 
 
```cpp 
git clone <url del repositorio> <nombre carpeta | opcional> 
ejemplos: 
git clone "https://github.com/sgtclean/clean1.git" // carpeta por defecto tiene el nombre del repositorio 
 
 
git clone "https://github.com/sgtclean/clean1.git" myrepositorio // se crea carpeta 'myrepositorio' 
``` 
 
 
2. Registro de cuenta GitHub 
> Es importante antes de hacer cualquier cambio al repositorio 
 
 
```cpp 
git config --global user.name "nombre a desplegar" 
git config --global user.email "correo asociado a GitHub" 
``` 
 
 
3. Enviar cambios al repositorio 
> Todo tu trabajo nuevo se debe actualizar y subir 
 
 
```cpp 
git add . // agrega los archivos recursivamente 
git commit -m "este es mi aporte al repositorio!" // mensaje que se despliega en GitHub 
git push  
git push --force // puedes omitir el mensaje, recomendado en cambios pequeños 
``` 
 
 
4. Actualizar cambios remotos y actualizarlos al repositorio local 
> Este comando es para actualizar el repositorio en tu computadora en caso de haber cambios en el repositorio por otro usuario o enviado remotamente 
 
 
```cpp 
git pull // actualizar los cambios en el repositorio y los descarga 
git pull --force // en caso de tener archivos mezclados, bien puedes forzar a que se actualice el repositorio sin que tengas que subir primero, posteriormente subes los demás archivos que no permitían el commit 
``` 
> Se recomienda hacer esto antes de hacer cambios 
 
 
## Visual studio code 
1. Tareas de vscode 
``` 
CTRL + P 
``` 
> Seleccionar run task 
[!alt text]() 
> Probar comando para correr Python 
[!alt text]() 
