#!/usr/bin/env python
#Desarrollado por: Antonio Orozco Ramirez antoniojorz@hotmail.com
#©Copyright 2018 Antonio Orozco Ramirez, Todos los derechos reservados bajo licencia GPL V3 https://www.gnu.org/licenses/gpl.html: cualquier modificacion 
#o cambio estructural del script se debe mantener el nombre del primer autor y el print de este.
#cualquier modificacion sobre el print es una violacion a los derechos de autor
#Este programa es software libre: puede redistribuirlo y / o modificar
#     bajo los términos de la Licencia Pública General de GNU publicada por
#     la Free Software Foundation, ya sea la versión 3 de la Licencia, o
#     (a su elección) cualquier versión posterior.

#     Este programa se distribuye con la esperanza de que sea útil,
#     pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
#     COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Ver el
#     Licencia pública general de GNU para más detalles.

#     Deberías haber recibido una copia de la Licencia Pública General de GNU
#     junto con este programa. De lo contrario, consulte <http://www.gnu.org/licenses/>
#
# Se autoriza toda copia y distribucion de este script siempre y cuando se mantenga los términos de la Licencia Pública General de GNU (GPL V3)
# Script Funcional con python3
# Se debe instalar las siguientes librerias:
# Se requiere la existencia del archivo url.txt
# Se requiere instalar los siguientes modulos para su funcionamiento
# pip install termcolor, pip install urllib3, pip install colorama pip install playsound
import urllib.request
import urllib.error
import time
import os
import ssl
import socket
import errno
#reproducir sonido
from playsound import playsound
#import httplib #este es para python2
from termcolor import *
#Para colorear en windows
import colorama
colorama.init()
#Para desastivar el check de SSL
ssl._create_default_https_context = ssl._create_unverified_context

__author__ = "Antonio Orozco R"
__copyright__ = "Copyright (C) 2018 Antonio Orozco R. antoniojorz@hotmail.com"
__license__ = "GPL/GNU V3"
__version__ = "1.1"
#======================================================================
#si requiere proxy dejar habilitado, sino comentar la siguiente linea
#export http_proxy='proxy:8080'
#======================================================================
#alarma
#siren = pygame.mixer.Sound("alarma1.mp3")
#abrir archivo
archivo = open("url.txt", "r")
#Contar numeros de lineas
iterlen = lambda it: sum(1 for _ in it)
cant = iterlen(open("url.txt"))
#ENCABEZADOS DE COLUMNAS
title_Fecha = "Fecha"
title_Url = "URL"
title_Estado = "Estado"
title_Razon = "Razon"
title_Tiempo = "Tiempo"
print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
cprint("Este script esta bajo licencia: "+__license__+" "+__copyright__,'white')
print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
#ASCII
print('  _____________  _____        _      __    __   ______       __  ')
print(' / ___/ __/ __ \/ ___/ ____  | | /| / /__ / /  / __/ /____ _/ /___ _____')
print('/ /___\ \/ /_/ / /__  /___/  | |/ |/ / -_) _ \_\ \/ __/ _ `/ __/ // (_-<')
print('\___/___/\____/\___/         |__/|__/\__/_.__/___/\__/\_,_/\__/\_,_/___/')
print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                      
cprint("%-25s %-80s %-30s %-7s" %(title_Fecha, title_Url, title_Estado, title_Tiempo),'white')
print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                      

while True:
	cantT=0
	TIMEOUT=8
	for site in archivo.readlines():
		#Borro los saltos de lineas
		if site[-1] == '\n':
			site = site[:-1]
		try:
			#Variables de conexion y estado
			opener = urllib.request.build_opener()
			opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			conn = opener.open(site, timeout=TIMEOUT)
			html_contents = conn.read()
			st = conn.code
			cantT+= 1
			#se calcula el tiempo transcurido para el check
			inicio = time.time()
			elapse_time = str(time.time()-inicio)[0:6]
			if conn.code in (200, 401, 301, 302):
				cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, st,elapse_time),'green')
			if conn.code in (408, 501, 503):
				cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, st,elapse_time),'yellow')
			#Reload
			if cantT == cant:
				#cierro archivo
				archivo.close()
				#reabro archivo
				archivo = open("url.txt", "r")
				#Contar numeros de lineas
				iterlen = lambda it: sum(1 for _ in it)
				cant = iterlen(open("url.txt"))
				print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
				cprint("Este script esta bajo licencia: "+__license__+" "+__copyright__,'white')
				print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
				#ASCII
				print('  _____________  _____        _      __    __   ______       __  ')
				print(' / ___/ __/ __ \/ ___/ ____  | | /| / /__ / /  / __/ /____ _/ /___ _____')
				print('/ /___\ \/ /_/ / /__  /___/  | |/ |/ / -_) _ \_\ \/ __/ _ `/ __/ // (_-<')
				print('\___/___/\____/\___/         |__/|__/\__/_.__/___/\__/\_,_/\__/\_,_/___/')
				print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                      
				cprint("%-25s %-80s %-30s %-7s" %(title_Fecha, title_Url, title_Estado, title_Tiempo),'white')
				print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                       
				conn.close()
		#Manejo de excepciones para timeout y otros errores		
		except urllib.error.URLError as e:
				if isinstance(e.reason, socket.timeout):
					cantT+= 1
					cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "Error Timeout",TIMEOUT),'red')
					#siren.play()
					playsound('alarma.mp3')
					#cierro archivo y conexion
					archivo.close()
					time.sleep(1)
					#reabro archivo
					archivo = open("url.txt", "r")
					#Reload
				if cantT == cant:
					#cierro archivo
					archivo.close()
					#reabro archivo
					archivo = open("url.txt", "r")
					#Contar numeros de lineas
					iterlen = lambda it: sum(1 for _ in it)
					cant = iterlen(open("url.txt"))
					print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
					cprint("Este script esta bajo licencia: "+__license__+" "+__copyright__,'white')
					print ('------------------------------------------------------------------------------------------------------------------------------------------------------')
					#ASCII
					print('  _____________  _____        _      __    __   ______       __  ')
					print(' / ___/ __/ __ \/ ___/ ____  | | /| / /__ / /  / __/ /____ _/ /___ _____')
					print('/ /___\ \/ /_/ / /__  /___/  | |/ |/ / -_) _ \_\ \/ __/ _ `/ __/ // (_-<')
					print('\___/___/\____/\___/         |__/|__/\__/_.__/___/\__/\_,_/\__/\_,_/___/')
					print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                      
					cprint("%-25s %-80s %-30s %-7s" %(title_Fecha, title_Url, title_Estado, title_Tiempo),'white')
					print ('------------------------------------------------------------------------------------------------------------------------------------------------------')                                       
					conn.close()
				elif e.reason != "algo":
					cantT+= 1
					cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "falló el nombre o el servicio, validar conexion a internet",TIMEOUT),'white')
					#cierro archivo y conexion
					archivo.close()
					time.sleep(1)
					#reabro archivo
					archivo = open("url.txt", "r")		
				elif e.error != "algo":
					cantT+= 1
					cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "falló el nombre o el servicio, validar conexion a internet",TIMEOUT),'white')
					#cierro archivo y conexion
					archivo.close()
					time.sleep(1)
					#reabro archivo
					archivo = open("url.txt", "r")						
				else:
					cantT+= 1
					cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, e.reason, elapse_time),'white')
					#cierro archivo y conexion
					archivo.close()
					time.sleep(1)
					#reabro archivo
					archivo = open("url.txt", "r")
		except socket.timeout:
				cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "Socket Timeout",TIMEOUT),'cyan')
				#siren.play()
				playsound('alarma.mp3')
				#cierro archivo y conexion
				archivo.close()
				time.sleep(1)
				#reabro archivo
				archivo = open("url.txt", "r")
		#except http.client.HTTPException as e:
		#		cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "Error de estado",e.reason),'yellow')
		#		#cierro archivo
		#		archivo.close()
		#		time.sleep(1)
		#		#reabro archivo
		#		archivo = open("url.txt", "r")
		except ConnectionResetError as e:
				conn.close()
				cantT+= 1
				cprint("%-25s %-80s %-30s %-7s" %(time.strftime("%c"),site, "Error de conexion" , elapse_time),'yellow')
				#cierro archivo
				archivo.close()
				time.sleep(1)
				#reabro archivo
				archivo = open("url.txt", "r")
	#Cierre de conexion y sleep	
	conn.close()
	time.sleep(3)