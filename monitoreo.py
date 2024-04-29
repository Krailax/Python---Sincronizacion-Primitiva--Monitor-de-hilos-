import threading
import time

class Estudiante(threading.Thread):
    def __init__(self, nombre_estudiante, n_progreso, semaforo_lectura, barrera_proyecto, barrera_final, lock):
        super().__init__()
        self.nombre_estudiante = nombre_estudiante
        self.n_progreso = n_progreso
        self.semaforo_lectura = semaforo_lectura
        self.barrera_proyecto = barrera_proyecto
        self.barrera_final = barrera_final
        self.lock = lock

    def leer(self):
        print(f"{self.nombre_estudiante}: Lectura en progreso...")
        for i in range(1, self.n_progreso + 1):
            with self.semaforo_lectura:
                print(f"{self.nombre_estudiante}: Progreso {i} de {self.n_progreso}")
            time.sleep(1)

        print(f"{self.nombre_estudiante}: Lectura completada.")

    def crear_idea_conjunta(self):
        print(f"{self.nombre_estudiante}: Creando idea conjunta...")
        # Simular tarea conjunta
        for i in range(1, 41):
            print(f"Creando idea - Progreso {i} de 40")
            time.sleep(0.1)

    def construir_idea_individual(self):
        print(f"{self.nombre_estudiante}: Construyendo idea individual...")
        # Simular tarea individual
        for i in range(1, 11):
            print(f"{self.nombre_estudiante}: Progreso {i} de 10")
            time.sleep(0.1)
        # Notificar que ha terminado la tarea individual
        with self.lock:
            print(f"Estudiante {self.nombre_estudiante}: Tarea individual completada.")

    def notificar_profesora(self):
        print(f"{self.nombre_estudiante}: Notificando a la su compañero que ha finalizado su parte...")

    def run(self):
        self.leer()
        self.barrera_proyecto.wait()
        self.crear_idea_conjunta()
        self.construir_idea_individual()
        self.barrera_final.wait()
        self.notificar_profesora()

# Crear objetos de sincronización
semaforo_lectura = threading.Semaphore(1)
barrera_proyecto = threading.Barrier(4)
barrera_final = threading.Barrier(4)
lock = threading.Lock()
# Crear instancias de los estudiantes
estudiante1 = Estudiante("1 Mateo", 10, semaforo_lectura, barrera_proyecto, barrera_final, lock)
estudiante2 = Estudiante("2 Ariel", 15, semaforo_lectura, barrera_proyecto, barrera_final, lock)
estudiante3 = Estudiante("3 Stefany", 13, semaforo_lectura, barrera_proyecto, barrera_final, lock)
estudiante4 = Estudiante("4 Camila", 17, semaforo_lectura, barrera_proyecto, barrera_final, lock)
# Iniciar los hilos de los estudiantes
estudiante1.start()
estudiante2.start()
estudiante3.start()
estudiante4.start()
# Esperar a que todos los estudiantes terminen
estudiante1.join()
estudiante2.join()
estudiante3.join()
estudiante4.join()
print("Proyecto completo. Notificando a la profesora...")