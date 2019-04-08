import os

'''Permite el ingreso de datos tipo string.'''
def ingreso_de_datos_str(cadena):
	mensaje=input(cadena)

	return mensaje
'''Permite el ingreso de datos tipo cadena y si comprueba que son números, 
   convierte el dato a tipo entero.'''
def ingreso_de_datos_int(cadena):
	opcion=input(cadena)
	while True:
		if opcion.isdigit()==False:
			opcion=input(cadena)
		else:
			opcion=int(opcion)
			return opcion
'''Menú de opciones de la interfaz del estacionamiento'''
def menu_de_opciones():

		print ("\n===========================================================")
		print ("===========================================================")
		print("1) Ingreso de auto.")
		print("2) Egreso de auto.")
		print("3) Consultar cantidad de autos estacionados actualmente.")
		print("4) Consultar cantidad de espacios disponibles.")
		print("5) Consultar o establecer el precio de estadia por dia.")
		print("6) Calcular lo que se debe facturar de estadia.")
		print("7) Fin del día. Facturar estadia.")
		print("8) Salir.")
		print ("===========================================================")
		print ("===========================================================\n")
'''Submenú de la opción 6 del menú principal.'''
def submenu():
	print ("==========================================================")
	print ("==========================================================")
	print("1) Establecer el precio por estadia del estacionamiento.")
	print("2) Consultar el precio por estadia del estacionamiento.")
	print ("==========================================================")
	print ("==========================================================")

'''Calcula lo que se debe facturar en concepto de estadía (en este caso, estadía por día).'''
def calcular_facturacion(autosEstacionados, precioEstadia):

		facturacionDia= precioEstadia * autosEstacionados

		return facturacionDia
