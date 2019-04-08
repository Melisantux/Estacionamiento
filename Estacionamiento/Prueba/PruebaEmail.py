import smtplib
import email.mime.text

class Servicio_externo():

	def enviarEmail(self, emisor, password, receptor, asunto, cuerpo):
		mensaje = MIMEText(cuerpo)
		mensaje['From'] = emisor
		mensaje['To'] = receptor
		mensaje ['Subject'] = asunto

		serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
		serverSMTP.ehlo() 
		serverSMTP.starttls() 
		serverSMTP.ehlo() 
		serverSMTP.login(emisor, password)

		serverSMTP.sendmail(emisor,receptor,mensaje.as_string())

		serverSMTP.close()