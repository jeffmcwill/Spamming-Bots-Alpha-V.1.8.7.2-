from whatsappspam import Whats
from SpamDiscord import SpamDiscord
from messegerbot import MessegerspamBot
from telegrambot import TelegramBot
import time

#-------------------------------------------------------------------------------------------------------------
#Spamming bots es un proyecto propio que reune ciertos bots para spamear mensajes en algunas redes sociales
#conocidas por el publico en general. Esta hecho enteramente en python 3, y se puede usar ejecutando el fichero
#SpammingBots.py. 
#-------------------------------------------------------------------------------------------------------------
# Nueva version lanzada 1.8.7.2 *Explicaciones en el README*
def Portada():
	print("""	    .andAHHAbnn. 
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I    
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH   
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP   Spamming Bots BY Jeff McWill
    "  `HK                   ]HH'  "         *Alpha 1.8.7.2*
        THAn.  .d.aAAn.b.  .dHHP       
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF        
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~" """)
	time.sleep(2)

def Main():
	opcion=0
	while opcion != 5:
		try:			
			print("""------------------------------------------------------------------------------------------
1. Whatsapp Spam Bot
(Recuerda estar conectado en Whatsapp Web por medio del Qr del vinculado a pc.)

2. Messenger "DM" Spam Bot 
(necesario estar logueado a facebook Y ID de la victima.)

3. Telegram Spam Bot 
(Requiere estar logueado en "web.telegram.org".)

4. Discord "Channel" and "DM" Spam Bot.
(requiere estar conectado a la version de escritorio de discord para sacar algunos parametros.)
------------------------------------------------------------------------------------------
5. Salir
------------------------------------------------------------------------------------------""")

			opcion=int(input("*Elije alguna Opcion: "))

			if opcion == 1:
				print("Iniciando Spam Whatsapp Bot...")
				time.sleep(1)
				Whats()
				break

			elif opcion == 2:
				print("Iniciando Spam Messenger Bot...")
				time.sleep(1)
				MessegerspamBot()
				break

			elif opcion == 3:
				print("Iniciando Spam Telegram Bot...")
				time.sleep(1)
				TelegramBot()
				break
				
			elif opcion == 4:
				print("Iniciando Spam Discord Bot...")
				time.sleep(1)
				SpamDiscord()
				break

			elif opcion == 5:
				print("----------------------------------")
				print("-¿Estas seguro que quieres salir?-")
				print("----------------------------------")
				opcion=int(input("1_Cerrar/ C/N_Volver al Menu: "))

				if opcion != 1:
					print("Volviendo al menu...")
					Main()
					break

				else:
					print("Hasta luego.")
					break

			else:
				print("No hay ninguna opcion seleccionada con ese caracter.")
				time.sleep(1)
				print("Volviendo al programa....")
				time.sleep(2)
		

		except:
			print("Caracteres no soportados, por favor ponga los indicados por el programa.")
			continue

if __name__=="__main__":
	Portada()
	Main()
