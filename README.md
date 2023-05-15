# 2023-1-Grupo-2

Finanzapp es una aplicación web creada utilizando Django. Actualmente cuenta con un sistema de usuarios que permite crear una cuenta e iniciar sesión. También permite ingresar transacciones al sistema, que pueden ser ingresos o gastos, y asignarles un valor y una descripción. Otra funcionalidad que con la que cuenta actualmente es el listado de transacciones, que muestra la información de cada una de las transacciones de un usuario, y permite editar los parámetros de una transacción o eliminarla del sistema.

Para correr la aplicación se necesita tener instaladas las librerías indicadas en el archivo *requirements.txt*, o instalarlas en un entorno virtual y activarlo para ejecutar la aplicación. Luego, se debe entrar a la carpeta *finanzapp_proj* ejecutar el comando.

```
python manage.py runserver
```

Esto iniciará la aplicación en la dirección *http://127.0.0.1:8000/*. Para crear una cuenta se debe agregar */register* al final de la dirección, y para iniciar sesión */login*. El resto de funcionalidades son accesibles desde la dirección inicial siempre y cuando se haya iniciado sesión.