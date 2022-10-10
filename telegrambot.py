import pyautogui,time
import webbrowser
import time

def TelegramBot():
	print("-------------------")
	print("- TelegramSpamBot -")
	print("-------------------")
	time.sleep(1)
	print("""Cosas a tener en cuenta:
--------------------------------------------
1.Debes estar logueado en web.telegram.org
2.Requiere el numero ID sin necesidad de "#"
3.Recuerda presionar en la barra "Message" para
que el bot envie los multiples mensajes, tiene un
retardo de 5 segundos.
--------------------------------------------""")
	time.sleep(1)
	apagado=0
	while apagado != 1:

		try:

			id=int(input("""Dime el numero de ID del usuario(sin "#"): """))

			mensajes=input("Que mensaje quieres enviar?: ")

			contador=int(input("Cuantas veces quieres spamear ese mensaje: "))

			webbrowser.open(f"https://web.telegram.org/z/#{id}")

			time.sleep(3)

			for i in range(contador):
				pyautogui.write(mensajes)
				pyautogui.press("enter")

			time.sleep(2)
			print("¿Quieres seguir usando este programa?")
			time.sleep(1)	
			apagado=int(input("C/N_Seguir en el programa/ 1_Apagar programa: "))

			if apagado != 1:
				print("Ok, continuemos...")
				time.sleep(2)
				TelegramBot()
				break

			else:
				print("Apagando...")
				time.sleep(1)
				print("Hasta luego.")
				break

		except:
			print("Falta algun parametro.")

if __name__=="__main__":
	TelegramBot()