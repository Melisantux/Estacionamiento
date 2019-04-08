class Parking_lot():

	def __init__(self):
		self.__totalPlazas = 100
		'''Diccionario en el que se guardarán el numero de plaza y su estado.'''
		self.__idEspacio = {}
		'''Por defecto, la plaza de estacionamiento se encuentra vacía.'''
		self.__autoEstacionado = False

		self.__lugaresDisponibles = 100

		self.__lugaresOcupados = 0

		'''Asigna un numero a cada plaza e indica que se encuentra vacía.'''
	def inicializarPlazas(self):
		for i in range(self.__totalPlazas):
			self.__idEspacio[i +1] = self.__autoEstacionado

		'''Se detecta que ingresa un auto y le asigna ocupado a la plaza.'''
	def ingresoDetectado(self, contadorAutosIngresados, totalAutosIngresados, cantidadAutosIngresados):
		for contadorAutosIngresados in range(totalAutosIngresados):
				self.__idEspacio[contadorAutosIngresados + 1] = self.__autoEstacionado=True

		print ("\n====================================================")
		print("Ingreso de ", cantidadAutosIngresados, " auto/s detectado.")
		print ("====================================================\n")

		'''Se detecta que egresa un auto y le asigna libre a la plaza.'''
	def egresoDetectado(self, contadorAutosEgresados, totalAutosEgresados, auxiliar):
		for contadorAutosEgresados in range(contadorAutosEgresados):
			self.__idEspacio[auxiliar] = self.__autoEstacionado=False
			contadorAutosEgresados = contadorAutosEgresados + 1
			auxiliar = auxiliar - 1

		print ("\n====================================================")
		print("Egreso de ", contadorAutosEgresados, " auto/s detectado.")
		print ("====================================================\n")

		'''Indica la cantidad de plazas que se encuentran libres.'''
	def espaciosDisponibles(self):
		espaciosDisponibles = 0
		for i in range(self.__totalPlazas):
			if self.__idEspacio[i+1] == False:
				espaciosDisponibles = espaciosDisponibles + 1

		print ("\n==================================================")
		print("Actualmente hay ", espaciosDisponibles, " espacio/s disponible/s.")
		print ("===================================================\n")

		'''Indica la cantidad de plazas que se encuentran ocupadas.'''
	def cantidadEstacionados(self):
		espaciosOcupados = 0
		for i in range(self.__totalPlazas):
			if self.__idEspacio[i+1] == True:
				espaciosOcupados = espaciosOcupados + 1
				
		print ("\n==================================================")
		print("Actualmente hay ", espaciosOcupados, " auto/s estacionado/s.")
		print ("===================================================\n")

		'''Comprueba la cantidad de autos que ingresan para asegurar que no superen la capacidad máxima del estacionamiento.'''
	def comprobacionEspacio(self, autosIngresados):

		if autosIngresados > 100:
			print("No quedan espacios disponibles.")
		else:
			return True