import os
import time
from ParkingLot import Parking_lot
from ServicioExterno import Servicio_externo
from Funciones import ingreso_de_datos_str, ingreso_de_datos_int, menu_de_opciones, submenu, calcular_facturacion

'''Declaración de acumuladores que se usarán para el control del ingreso y egreso de autos'''
acumuladorAutosIngresados=0
totalAutosIngresados=0

acumuladorAutosEgresados=0
totalAutosEgresados=0

'''Para determinar si se debe ejecutar el condicional para realizar el ingreso del auto o no.'''
comprobacion = False

'''Para determinar si se estableció previamente un precio de estadía o no.'''
flagEstadia=True

estacionamiento = Parking_lot()
estacionamiento.inicializarPlazas()

while True:
	menu_de_opciones()
	
	opcion=ingreso_de_datos_int("Ingrese la opción deseada: ")
	
	while opcion<0 or opcion>8:
		opcion=ingreso_de_datos_int("Error. Ingrese una opción válida: ")

	if(opcion==1):

		os.system('cls')

		cantidadAutosIngresados=ingreso_de_datos_int("\nIndique la cantidad de autos que ingresan al estacionamiento: ")

		while cantidadAutosIngresados <=0 or cantidadAutosIngresados > 100:
			if cantidadAutosIngresados <=0:
				cantidadAutosIngresados=ingreso_de_datos_ints("\nError. Ingrese una cantidad de autos mayor que cero: ")
			else:
				cantidadAutosIngresados=ingreso_de_datos_int("\nError. Ingresó una cantidad de autos que supera la capacidad máxima del estacionamiento.\n\nIndique la cantidad de autos que ingresan al estacionamiento: ")

		totalAutosIngresados= totalAutosIngresados + cantidadAutosIngresados

		comprobacion = estacionamiento.comprobacionEspacio(totalAutosIngresados)

		if comprobacion:
			acumuladorAutosIngresados=acumuladorAutosIngresados + cantidadAutosIngresados
			estacionamiento.ingresoDetectado(acumuladorAutosIngresados, totalAutosIngresados, cantidadAutosIngresados)
		else:
			totalAutosIngresados= totalAutosIngresados - cantidadAutosIngresados

		os.system('pause')
		os.system('cls')

	elif(opcion==2):

		os.system('cls')

		if totalAutosIngresados == 0:
			print("\n======================================================================================")
			print("Error. No se pueden realizar egresos porque el estacionamiento se encuentra vacío.")
			print ("======================================================================================\n")
		else:
			cantidadAutosEgresados=ingreso_de_datos_int("\nIngrese la cantidad de autos que se van del estacionamiento: ")

			while cantidadAutosEgresados > totalAutosIngresados or cantidadAutosEgresados <= 0:
				if cantidadAutosEgresados <= 0:
					cantidadAutosEgresados=ingreso_de_datos_int("\nError. Ingrese una cantidad de autos que se van del estacionamiento mayor que cero: ")
				else:
					cantidadAutosEgresados=ingreso_de_datos_int("\nError. La cantidad de autos estacionados es menor a cantidad de autos que ingresó para hacer la salida.\n\nIngrese una cantidad correcta: ")

			totalAutosEgresados= totalAutosEgresados + cantidadAutosEgresados

			estacionamiento.egresoDetectado(cantidadAutosEgresados, totalAutosEgresados, totalAutosIngresados)

			totalAutosIngresados = totalAutosIngresados - cantidadAutosEgresados

		os.system('pause')
		os.system('cls')

	elif(opcion==3):
		os.system('cls')

		estacionamiento.cantidadEstacionados()
		os.system('pause')
		os.system('cls')

	elif(opcion==4):
		os.system('cls')

		estacionamiento.espaciosDisponibles()

		os.system('pause')
		os.system('cls')


	elif(opcion==5):
		os.system('cls')

		submenu()
		subOpcion=ingreso_de_datos_int("\nIngrese la opcion deseada: ")

		while (subOpcion < 1) or (subOpcion > 2):
			subOpcion=ingreso_de_datos_int("\nError. Ingrese una opcion valida: ")

		if subOpcion == 1:
			precioEstadia=ingreso_de_datos_int("\nEstablezca el precio de estadia por dia: ")
			flagEstadia=False

		else:
			if flagEstadia:
				print ("\n==========================================================")
				print("Error. Usted no ha establecido ningun precio de estadia.")
				print ("===========================================================\n")
				os.system('pause')
			else:
				print ("\n====================================================")
				print("El precio de estadia por dia es: ", precioEstadia)
				print ("====================================================\n")
				os.system('pause')
		os.system('cls')

	elif(opcion==6):
		if flagEstadia:
			print ("\n===========================================================")
			print("Error. Usted no ha establecido ningun precio de estadia.")
			print ("===========================================================\n")
		else:
			facturacion = calcular_facturacion(totalAutosIngresados, precioEstadia)

			print ("\n========================================================================================")
			print("Actualmente se debe facturar un total de ", facturacion, " en concepto de estadía.")
			print ("========================================================================================\n")

		os.system('pause')
		os.system('cls')

	elif(opcion==7):

		if flagEstadia:
			print ("\n===========================================================")
			print("\nError. Usted no ha establecido ningun precio de estadia.")
			print ("===========================================================\n")
			os.system('pause')
			os.system('cls')
		else:
			os.system('cls')
			print ("\n======================================================")
			print("Dia finalizado.")
			print("Enviar email con la facturacion del dia al encargado.")
			print ("========================================================\n")

			facturacionDia = calcular_facturacion(totalAutosIngresados, precioEstadia)

			email = Servicio_externo()
			emailEncargado = ingreso_de_datos_str("Ingrese el email del encargado: ")
			contador = 0
			while True:
				for i in emailEncargado:
					if i=="@" or i==".":
						contador = contador + 1
				if contador >= 2:
					break
				else:
					emailEncargado = ingreso_de_datos_str("\nError, ingrese un email valido: ")

			asunto=ingreso_de_datos_str("\nIngrese el asunto del email a enviar: ")

			cuerpoEmail="\nLe envio la facturacion correspondiente al cierre de hoy.\nEl monto total de las estadias es: " + str(facturacionDia) + " correspondiente a \n" + str(totalAutosIngresados) + " autos que se encontraban estacionados al momento de cerrar."

			email.enviarEmail(asunto, cuerpoEmail, emailEncargado)

	else:
		print ("\n====================================================")
		print("Finalizando programa")
		print ("====================================================\n")

		time.sleep(1)
		break