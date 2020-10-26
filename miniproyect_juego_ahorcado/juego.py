def juego():

	from palabra_al_azar import palabra #importo la palabra aleatoria desde el archivo palabra_al_azar
	from archivos_dibujo import errores #importo la funcion errores del archivo --> archivos_dibujo
	#generamos palabra aleatoria de la lista
	palabra = palabra() #paso el retorno de la palabra aleatoria a una variable
	




	tu_palabra = "" #creo una variable donde voy a meter las letras del jugador
	
	

	fallos = 1 
	intentos = 9
	
	while fallos <=10:
		contador_fallo = 0
		

		for letra in palabra:
			if letra in tu_palabra:
				print(letra,end="") #recorro la iteracion por la palabra, si esta en mi  variable tu palabra pondre las letras
				                    #que estan en la palabra aleatoria seguidas
			else:
				print("*",end="")   #en caso de que no esten se pondran asteriscos seguidos y se sumara uno al contador
				contador_fallo += 1
		if contador_fallo == 0: #no habras tenido ningun fallo
			print("\n ------------------------------Ganaste!!!!!!!!!!!!!!!!!")
			break
		
		letra_jugador = input("\nDiga una letra: ")
		tu_palabra+=letra_jugador.lower() #añado las letras del jugador a la variable tu palabra

		if tu_palabra == palabra:
			print("\n     --------------------Ganaste!!!!!!!!!!!!!!")
			break
		
		if letra_jugador.lower() not in palabra:
			
			print(errores("ficheros_dibujo/" + str(fallos) + ".txt")) #meto la funcion errores importada y por bucle me genera
			                                                            #un segundo archivo para ir recreando todos.
			fallos +=1  #sumo uno a los intentos para que vaya llegando a 9 si no se encuentra la letra
			intentos -= 1 # resto menos uno de la variable intentos para que vaya llegando a 0.
			print("Lastima, me temo que no está...Te quedan",intentos,"intentos.")
		else:
			print("Vamos!!!\n")
			
		

		 
		if intentos == 0: # si el contador de fallos es igual a 0, que
			print("\nPerdiste!!!!!!\n")
			break
			
		

	repetir = input("Quieres jugar otra? S/N: ")
	if repetir.upper() == "S":
		juego()
	elif repetir.upper() == "N":
		print("Hasta otra!!!!!")
	else:
		print("Lo siento, no es la respuesta que esperaba... Asique Adiós Xao bella!!!!")