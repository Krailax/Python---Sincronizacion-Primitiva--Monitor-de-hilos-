# Pasos para ejecución de la plataforma web hecha en Django

No olviden dejar su estrellita en el repositorio de GitHub. ¡Apoyen!

## Instalación de Python

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargar la última versión desde https://www.python.org/

2. Crear un entorno virtual con :
   > python -m venv entornoVirtual


3.0 Verificar la Política de Ejecución Actual:
   Para saber cuál es la política de ejecución actual, abre PowerShell y ejecuta:
   > Get-ExecutionPolicy
   Para cambiar la política a Unrestricted, ejecuta:
   > Set-ExecutionPolicy Unrestricted

3. Activación del entorno virtual
   Revisar la caperta que hay dentro entornoVirtual puede haber dos variable que la caperta se llame Script o bin según ellos activará el comando que corresponde.
   
   > entornoVirtual\Scripts\activate
   > entornoVirtual\bin\activate

5. Instalamos la librerías que se encuentra en requirements.txt
   > pip install -r requirements.txt

6. Entras a la caperta sincronizacionPrimitiva
   > cd ./sincronizacionPrimitiva

7. Levantamos el servidor de Django
   > py manage.py runserver

# Fin
¡Listo para ejecutar tu plataforma web! Si tienes algún problema, asegúrate de seguir estos pasos correctamente. ¡Buena suerte!
