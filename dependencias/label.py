class tarea:
    numero_tarea = 0
    titulo_tarea = ""
    descripcion_tarea = ""
    tarea_completada = 0
    def __init__(self, num, tit, des):
        self.numero_tarea = num
        self.titulo_tarea = tit
        self.descripcion_tarea = des
    
    def self_print(self):
        if self.tarea_completada == 0:
            print(self.numero_tarea, self.titulo_tarea, self.descripcion_tarea)
        else:
            print("Tarea numero", self.numero_tarea, "completada ~")

lista_tareas = [
    tarea(1, "Crear un hola mundo", "Principalmente es entender la organizacion del proyecto"),
    tarea(2, "Crear un interprete de polinomios", "El proposito de este programa es generar ")
]

def imprimir_label():
    for i in range(len(lista_tareas)):
	    lista_tareas[i].self_print()

def instrucciones_tarea(val):
    if val <= len(lista_tareas):
        lista_tareas[val].self_print()
    else:
        print("La tarea no existe")

def complete_tarea(val):
    if val <= len(lista_tareas):
        lista_tareas[val].tarea_completada = 1
    else:
        print("La tarea no existe")