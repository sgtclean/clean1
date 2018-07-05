from dependencias.label import *
from dependencias.cano.tareas import task1
import os

def version_de_ayuda():
	instrucciones_tarea(0)
	task1()
	complete_tarea(0)

def tu_version_de_main():
	pass

if __name__ == '__main__':
	version_de_ayuda()
	tu_version_de_main()
	imprimir_label()