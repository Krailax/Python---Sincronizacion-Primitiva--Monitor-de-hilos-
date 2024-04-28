import threading
import time

class Alumno(threading.Thread):
    def __init__(self, nombre, profesora):
        super().__init__()
        self.nombre = nombre
        self.paginas_leidas = 0
        self.leido = threading.Event()  # Evento para indicar que el alumno ha terminado de leer
        self.trabajando = threading.Event()  # Evento para indicar que el alumno está trabajando
        self.profesora = profesora

    def leer_libro(self):
        for i in range(1, 13):  # Suponiendo que el libro tiene 12 páginas
            time.sleep(1)  # Simula la lectura de una página
            self.paginas_leidas = i
        self.leido.set()  # Indica que el alumno ha terminado de leer

    def trabajar(self):
        time.sleep(5)  # Simula el trabajo del alumno
        self.trabajando.set()  # Indica que el alumno ha terminado de trabajar

    def run(self):
        self.leer_libro()
        self.leido.wait()  # Espera a que el alumno termine de leer
        self.profesora.notificar_leido()  # Notifica a la profesora que ha terminado de leer
        self.trabajar()
        self.trabajando.wait()  # Espera a que el alumno termine de trabajar
        self.profesora.notificar_trabajo()  # Notifica a la profesora que ha terminado de trabajar

class Profesora:
    def __init__(self, alumnos):
        self.alumnos = alumnos
        self.trabajos_completados = 0

    def monitorear_leer(self):
        for alumno in self.alumnos:
            alumno.join()  # Espera a que el alumno termine de leer
        print("Todos los alumnos han terminado de leer el libro.")

    def notificar_leido(self):
        print(f"{self.alumnos[self.trabajos_completados].nombre} ha terminado de leer.")
        self.trabajos_completados += 1

    def monitorear_trabajar(self):
        for alumno in self.alumnos:
            alumno.join()  # Espera a que el alumno termine de trabajar
        print("Todos los alumnos han terminado de trabajar en la idea.")

    def notificar_trabajo(self):
        print(f"{self.alumnos[self.trabajos_completados].nombre} ha terminado de trabajar en la idea.")
        self.trabajos_completados += 1

# Crear instancias de alumnos
alumno1 = Alumno("Alumno 1", None)
alumno2 = Alumno("Alumno 2", None)
alumno3 = Alumno("Alumno 3", None)
alumno4 = Alumno("Alumno 4", None)

# Crear instancia de profesora y asignarla a los alumnos
profesora = Profesora([alumno1, alumno2, alumno3, alumno4])
for alumno in profesora.alumnos:
    alumno.profesora = profesora

# Iniciar la lectura del libro
print("La profesora inicia la lectura del libro.")
for alumno in profesora.alumnos:
    alumno.start()

profesora.monitorear_leer()  # Monitorear la lectura de los alumnos

# Iniciar el trabajo en la idea
print("La profesora inicia el trabajo en la idea.")
for alumno in profesora.alumnos:
    alumno.start()

profesora.monitorear_trabajar()  # Monitorear el trabajo en la idea
