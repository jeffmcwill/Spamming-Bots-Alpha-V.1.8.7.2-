import pyautogui, webbrowser
from time import sleep

#se agrega el id del chat del usuario que queremos spamear.

def MessegerspamBot():
	apagado=0
	print("-------------------")
	print("- MessegerspamBot -")
	print("-------------------")
	sleep(1)
	print("""Cosas a tener en cuenta:
----------------------------------------------------------------------------
1.Requiere del ID del usuario(donde se pone las direcciones DNS
2.Necesario estar logueado a la cuenta de messeger a la que quieres Spammear
3.Manten presionado con el cursor izquierdo la barra de mensajes de la victima
a spammear. por cuestiones de Bugs, a veces no funciona adecuadamente y se
selecciona por otra parte.
4.Solo funciona en la version web de Facebook Messenger.
----------------------------------------------------------------------------""")
	sleep(1)
	while apagado != 1:
		
		try:

			id=input("Dime el ID usuario (Esquina superior): ")
			
			mensaje=input("Que mensaje deseas spamear: ")
			
			repeticiones=int(input("Cuantas veces?: "))

			#pestaña que abre en el navegador.
			webbrowser.open(f"https://www.facebook.com/messages/t/{id}")

			sleep(5)

			#------------------------------
			for i in range(repeticiones):
				pyautogui.write(mensaje)
				pyautogui.press('enter')
			#------------------------------
			#100010715145070

			sleep(2)
			print("¿Quieres seguir usando este programa?")	
			sleep(1)
			apagado=int(input("C/N_Seguir en el programa/ 1_Apagar programa: "))

			if apagado != 1:
				print("Ok, continuemos...")
				sleep(2)
				MessegerspamBot()
				break

			else:
				print("Apagando...")
				sleep(1)
				print("Hasta luego.")
				break
		except:
			print("Id no encontrado o caracteres no soportados.")

if __name__=="__main__":
	MessegerspamBot()