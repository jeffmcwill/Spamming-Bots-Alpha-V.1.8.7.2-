import pyautogui
import time
import webbrowser

def Whats():
	apagado=0
	print("--------------------------")
	print("- Whatsapp Spamming Bot. - ")
	print("--------------------------")
	time.sleep(1)
	print("""Cosas a tener en cuenta:
-----------------------------------------------------------------------------
1.Recuerda agregar el numero con el "+" aqui ejemplo +54xxxxxxxxxxx
2.Siempre poner el numero del codigo del pais. en caso de argentina "+54"
3.Es requerido que el usuario que queramos spammear tenga cuenta en whatsapp.
4.El limite de mensajes spam es de 300.
-----------------------------------------------------------------------------""")
	time.sleep(1)
	while apagado != 1:
		try:
			numerodetelefono=input("*Dime el numero de telefono*: ")
			#se agrega aqui el numero de telefono.
			
			print("........................")
			mensaje1=input("*Que mensaje deseas enviar?*: ")

			#se agrega el mensaje que quieras agregar.
			print("........................")

			contador=int(input("*Dime cuantos mensajes quieres spammear*: "))
				
			url='https://web.whatsapp.com/send?phone='
			#se usa esto para añadir la url del whatsapp web.

			webbrowser.open(url+numerodetelefono)

			time.sleep(8)
			#algoritmo de spamming
			#------------------------------
			for i in range(contador):
				pyautogui.write(mensaje1)
				pyautogui.press('enter')
			#------------------------------

			time.sleep(2)
			print("¿Quieres seguir usando este programa?")
			time.sleep(1)
			apagado=int(input("C/N_Seguir en el programa/ 1_Apagar Programa: "))

			if apagado != 1:
				print("Ok, continuemos...")
				time.sleep(2)
				Whats()
				break

			else:
				print("Apagando...")
				time.sleep(1)
				print("Hasta luego.")
				break

		except:
			print("Numero desconocido o no encontrado, trata de poner el numero nuevamente.")

if __name__=="__main__":
	Whats()