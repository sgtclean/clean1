class tarea:
    numero_tarea = 0
    titulo_tarea = ""
    descripcion_tarea = ""
    def __init__(self, num, tit, des):
        self.numero_tarea = num
        self.titulo_tarea = tit
        self.descripcion_tarea = des
    
    def self_print(self):
        print(self.numero_tarea)

todoList = [
    tarea(1, "crear un hola mundo", "mas descripcion")
]