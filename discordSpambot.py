import requests
import json
import time

def DiscordSpam():
	apagado=0
	print("--------------------")
	print("- Spam Discord Bot -")
	print("--------------------")
	time.sleep(1)
	while apagado != 1:
		print("""Cosas a tener en cuenta:
--------------------------------------------------------------------------------------
1.Tienes que tener tu cuenta de discord en modo Desarrollador para poder conseguir el codigo 
"ID".

2.Para conseguir el token debes ir a tu navegador, poner tu cuenta en la version web de
discord,ir a la casilla mensajes de tu parte superior izquierda, luego en a tu derecha en
"Chrome" aprieta la casilla de los tres puntos, ve hasta abajo y presiona "Mas Herramientas",
alli presiona "Herramientas del desarrollador", ahi a tu izquierda ve en "Local Storage" y 
https//:discord.com, en el buscador superior pon "token", copia ese codigo tal cual esta, solo
quitando las "Comillas" que estan en su costado.

3.El archivo TXT que viene en el programa deberas de modificarlo antes de ejecutar este codigo
ahi añadele todos los mensajes que quieras agregar.(desabilitado)

4.Esta en face "Experimental",tiene bugs como que el programa se quede spameando infinitamente
hasta que el usuario cierre el EXE de discord o simplemnte apague la computadora. no se a cuanto
puede llegar con la utilizacion de RAM en la pc, usarlo bajo su propio riesgo.(en alguna futura
version corregire este bug.)
--------------------------------------------------------------------------------------""")

		#aca iria el ID del canal donde vamos a spamear
		time.sleep(1)
		channel_ID=int(input("*Dime el codigo ID del canal de texto donde quieres spammear: "))
		
		#este token lo buscamos en la web de discord.

		headers={}

		print("------------------------------------------------------------------------------------")
		print("""En caso que no se entendio la explicacion te dejo un link para encontrar el token:
https://www.youtube.com/watch?v=LnBnm_tZlyU""")
		print("------------------------------------------------------------------------------------")

		headers1=input("*Codigo token de tu cuenta(Recomendable guardarlo en algun archivo aparte): ")

		#este codigo despues se guarda en el diccionario para ser ejecutado.
		headers["authorization"] = headers1

		print("------------------------------------------------------------")
		print("""Advertencia: los mensajes que se envien seran infinitos por ende
nunca se detendra, requeriras cerrar la ventana de este programa para elegir
las opciones.""")
		mensaje = input("*Que mensaje deseas enviar?*: ")
		#se agrega el mensaje que quieras agregar.
		print("------------------------------------------------------------")

		#contador = int(input("*Dime cuantos mensajes quieres spammear*: "))

		print("Cargando...")

		time.sleep(2)
		print("Para terminar de ejecutarlo cierra esta ventana(se quedara ejecutando infinitamente).")
		time.sleep(1)
		while True:	
			for i in range(1000):
				requests.post(f"https://discord.com/api/v9/channels/{channel_ID}/messages", headers = headers,json = {"content":mensaje})

		print("Hecho.")
		

if __name__=="__main__":
	DiscordSpam()


