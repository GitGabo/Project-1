import os
import json
os.system('clear')
#Ejercicio 33

#cargar archivo json
with open("info.json", "r") as f:
    database = json.load(f)
#guardar archivo json
def guardar(nombre_archivo, database):
	with open(nombre_archivo, 'w') as f:
		json.dump(database, f)
#mostrar la lista de personas
def mostrar_personas(database):
	print ''
	for i in database.keys():
		print '-', i
	print ''

#dar la respuesta de la fecha del cumple
def dar_respuesta(database, persona):
	if persona in database:
		print 'El cumple de ', persona, ' es el ', database[persona]

si_no = 'si'
while si_no == 'si':
	os.system('clear')
	print 'Este es un programa de perfiles.\nActualmente tenemos disponibles a las siguientes personas:'
	mostrar_personas(database)
	elegir = raw_input('Quiere buscar o agregar un cumple? >>> ').lower()
	#AGREGANDO NOMBRE
	if elegir == 'agregar':
		os.system('clear')
		print 'Ingrese el nombre de la persona que desea agregar'
		agregar_nombre = raw_input('>>> ').title()
		#EL NOMBRE NO ESTA EN LA BASE DE DATOS
		if agregar_nombre not in database:
			print ''
			print 'Ahora ingrese la fecha del cumple de', agregar_nombre
			agregar_fecha = raw_input('>>> ')
			database[agregar_nombre] = agregar_fecha
			#SE GUARDAN LOS DATOS EN EL ARCHIVO JSON
			guardar('info.json', database)
			print ''
			print 'Listo!'
			si_no = raw_input('Volver al inicio? >>> ')
		else:
			#EL NOMBRE ESTA EN LA BASE DE DATOS
			os.system('clear')
			print 'El perfil de', agregar_nombre, 'ya esta en la base de datos!'
			print ''
			print 'Desea modificarlo?'
			modi_o_dejar = raw_input('>>> ')
			#LA PERSONA ELIGIO MODIFICAR
			if modi_o_dejar == 'si':
				print 'Por favor ingrese la nueva fecha del cumple de', agregar_nombre
				print ''
				modi_fecha = raw_input('>>> ')
				database[agregar_nombre] = modi_fecha
				#SE GUARDAN LOS DATOS EN EL ARCHIVO JSON
				guardar('info.json', database)
				print 'Actualizado!'
				si_no = raw_input('Volver al inicio? >>> ')
			else:
				#LA PERSONA ELIGIO NO MODIFICAR Y EL PROGRAMA DA LA OPCION DE VOLVER
				print 'Okey!'
				si_no = 'si'
	#LA PERSONA ELIGIO BUSCAR
	elif elegir == 'buscar':
		os.system('clear')
		print 'Que cumple quiere buscar?'
		mostrar_personas(database)
		buscador = raw_input('>>> ').title()
		#CICLO QUE SE ABRE MIENTRAS LA PERSONA NO ESTE EN LA BASE DE DATOS
		while buscador not in database:
			os.system('clear')
			print 'Esa persona no esta en la base de datos!'
			print 'Que cumple quiere buscar?' 
			mostrar_personas(database)
			buscador = raw_input('>>> ').title()
		else:
			#SE DA LA RESPUESTA Y PREGUNTA SI QUIERE VOLVER AL INICIO
			print ''
			dar_respuesta(database, buscador)
		print ''
		si_no = raw_input('Quiere volver al inicio? >>> ')
	#LA PERSONA ELIGION ELIMINAR
	elif elegir == 'eliminar':
		os.system('clear')
		print '----------------------------------------------------'
		print '(CUIDADO! ELIMINAR UN PERFIL NO PUEDE SER DESHECHO!)'
		print '----------------------------------------------------'
		print 'A quien quiere eliminar de esta lista?'
		mostrar_personas(database)
		elegir_eliminar = raw_input('>>> ').title()
		#EL PROGRAMA BUSCA PARA VER SI LA PERSONA ESTA EN LA BASE DE ATOS
		if elegir_eliminar in database:
			print ''
			print 'Esta seguro de querer eliminar el perfil de', elegir_eliminar,'?'
			confirmar = raw_input('>>> ').lower()
			#SI ESTA EN LA BASE DE DATOS, EL PROGRAMA ESPERA UNA CONFIRMACION PARA BORRAR EL PERFIL
			if confirmar == 'si':
				#SE ELIMINA EL PERFIL Y SE GUARDA
				del database[elegir_eliminar]
				guardar('info.json', database)
				print ''
				print 'Eliminado!'
				si_no = raw_input('Quiere volver al inicio? >>> ')
			else:
				#LA PERSONA DECIDIO NO ELIMINAR EL PERFIL
				print 'Usted no elimino el perfil'
				si_no = raw_input('Quiere volver al inicio? >>> ')
		else:
			#EL PERFIL QUE LLA PERSONA BUSCO NO ESTA EN LA BASE DE DATOS
			print ''
			print elegir_eliminar, 'no esta en la base de datos!'
			si_no = raw_input('Volver al inicio? >>> ')
	elif elegir == 'cerrar' or elegir == 'salir':
		si_no = 'no'
os.system('clear')
print 'Okey'
