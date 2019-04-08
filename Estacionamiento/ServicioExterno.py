import os
import time

class Servicio_externo():

	def enviarEmail(self, asunto, cuerpo, email):

		print ("\n=================================================================")
		print("Asunto:", asunto)
		print("Para:", email)
		print(cuerpo)
		print ("=================================================================\n")

		print ("\n====================================================")
		print("Enviando email...")
		print ("====================================================\n")

		time.sleep(3)

		os.system('pause')
		os.system('cls')

		print ("\n=====================================================================================================")
		print("Email con la facturacion del dia enviado con éxito a la direccion ", email, " .")
		print ("======================================================================================================\n")

		os.system('pause')
		os.system('cls')

