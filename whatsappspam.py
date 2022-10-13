import pyautogui
import time
import webbrowser

#mejorado los parametros de whatsapp y mayores explicaciones para que puedan usarlo bien. #12/10/22

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
4.El limite de mensajes spam es ilimitado, pero ve sabiendo que esto puede afectar
gravemente al dispositivo de la victima.
5.Para mas eficiencia siempre hazlo en ambientes controlados.
6.Manten siempre presionado la caja de texto en whatsapp para que el bot haga 
eficientemente su trabajo.
-----------------------------------------------------------------------------""")
	time.sleep(1)
	while apagado != 1:
		try:
			numerodetelefono=input("*Dime el numero de telefono*: ")
			#se agrega aqui el numero de telefono.
			
			print("--------------------------------------")
			mensaje1=input("*Que mensaje deseas enviar?*: ")

			#se agrega el mensaje que quieras agregar.
			print("--------------------------------------")

			contador=int(input("*Dime cuantos mensajes quieres spammear*: "))
			print("--------------------------------------")	
			url='https://web.whatsapp.com/send?phone='
			#se usa esto para añadir la url del whatsapp web.
			print("Mantiene presionado la caja de texto...")
			webbrowser.open(url+numerodetelefono)

			time.sleep(8)

			print(f"Enviando mensajes a {numerodetelefono}")
			print("--------------------------------------")
			time.sleep(2)
			#algoritmo de spamming
			#------------------------------
			for i in range(contador):
				pyautogui.write(mensaje1)
				pyautogui.press('enter')
			#------------------------------

			time.sleep(2)
			print("--------------------------------------")
			print("¿Quieres seguir usando este programa?")
			print("--------------------------------------")
			time.sleep(1)
			apagado=int(input("C/N_Seguir en el programa/ 1_Apagar Programa: "))

			if apagado != 1:
				print("--------------------------------------")
				print("Ok, continuemos...")
				print("--------------------------------------")
				time.sleep(2)
				Whats()
				break

			else:
				print("--------------------------------------")
				print("Apagando...")
				time.sleep(1)
				print("Hasta luego.")
				print("--------------------------------------")
				break

		except:
			print("Numero desconocido o no encontrado, trata de poner el numero nuevamente.")
			print("--------------------------------------------------------------------------")

if __name__=="__main__":
	Whats()
