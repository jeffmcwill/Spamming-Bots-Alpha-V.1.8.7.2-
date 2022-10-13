import pyautogui
import time

#nueva version corregida alpha 1.8.7
#ahora es mas sencillo usar este bot.

def SpamDiscord():
	exit=0
	while exit != 1:		
		print("------------------------------")
		print("""//_Spameador de Discord_// 
-------------------------------------------------------------------------------- 
_instrucciones de uso:
1.Siempre que se este ejecutando presionar la casilla de mensajes de la victima.
o canal donde vayamos a spamear.
2.Tener cuidado con esta herramienta, su uso es solo para pruebas de seguridad. no me 
hago responsable del mal uso que le des.
3.En limite del spam es incalculable, pero por ciertos motivos discord suele ponerte
un limite de 30 mensajes, en esta version del programa he puesto un modo lento automatico 
cuando superes los ese limite.
4.Siempre mantiene el cursor presionando la barra de mensajes de discord, si tu lo sacas
el bot dara error y comenzara de nuevo, ten en cuenta ese pequeño detalle.
--------------------------------------------------------------------------------""")
		time.sleep(1)
		print("Prueba de seguridad de canales o DMs de Discord by Jeff MCWill")
		time.sleep(1)
		print("--------------------------------------------")
		mensaje=input("Dime que mensaje quieres spamear: ")
		time.sleep(1)
		print("-------------------------------------------")
		
		try:

			repeticiones=int(input("¿Cantidad de mensajes?: "))

			if repeticiones > 30:
				print("la cantidad de mensajes supera los 30, asi que se activara el modo lento")
				print("--------------------------------------")
				print("Presiona la barra de mensajes de discord.")
				time.sleep(2)
				print("--------------------------------------")
				print("Tienes 5 segundos... Apurate.")
				time.sleep(5)

				for i in range(repeticiones):
					pyautogui.write(mensaje)
					pyautogui.press('enter')
					time.sleep(1)


				print("--------------------------------------")
				print("Ejecucion de comandos finalizada...")
				print("--------------------------------------")	

				exit=int(input("Deseas salir? Press 1_ Si o Cual/Num para No: "))
				if exit == 1:
					break
				else:
					SpamDiscord()
					break

			elif repeticiones <= 30:
				print("La cantidad de mensajes es menor a 30, se activo el modo rapido.")
				time.sleep(1)
				print("--------------------------------------")
				print("Presiona la barra de mensajes de discord.")
				time.sleep(2)
				print("--------------------------------------")
				print("Tienes 5 segundos... Apurate.")
				time.sleep(5)

				for i in range(repeticiones):
					pyautogui.write(mensaje)
					pyautogui.press('enter')

				print("--------------------------------------")
				print("Ejecucion de comandos finalizada...")
				print("--------------------------------------")

				exit=int(input("Deseas salir? Press 1_ Si o Cual/Num para No: "))
				if exit == 1:
					print("Hasta luego.")
					time.sleep(1)
					break
				else:
					print("Cargando...")
					time.sleep(1)
					SpamDiscord()
					break
		except:
			print("Caracteres no soportados. AÑada SOLO numeros.")					

if __name__=="__main__":
	SpamDiscord()

