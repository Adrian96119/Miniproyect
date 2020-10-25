
from pregunta_nombre import pregunta_nombre 
from edad import edad
print("\n\n") #Hago dos saltos de linea para que no me quede tan arriba el texto
print("                     -------------------********¡JUEGO DEL AHORCADO!********---------------------") 
#espaceo el titulo para que me quede más bonito
print("\n  DESCRIPCION DEL JUEGO---->>>>\n")
print("""  Vamos a jugar al conocidísimo juego del ahorcado, el de toda la vida.\n
	La computadora elegirá una palabra al azar que usted debera adivinar. Irá eligiendo una letra por cada
	ronda. Si la letra se encuentra dentro de la palabra elegida, se colocará en un conjunto de lineas vacias
	que representan la palabra sin determinar, y si no está, se añadirá un caracter para representar el dibujo del
	hombre ahorcado.\n""")
print("  OBJETIVO DEL JUEGO---->>>>\n")
print(" Debe llegar a adivinar la palabra completa antes de que el dibujo del ahorcado se complete\n")
print("""  REGLAS:
                 -Si repite una letra, contará como errónea y se añadirá otro caracter al ahorcado.
                 -Tiene de limite 12 letras antes de que se complete el dibujo entero
                 -No hay posibilidad de comodín, no te calientes.\n""")
print("       QUE EMPIECE EL JUEGO...")

pregunta_nombre() #Importo funcion de pregunta_nombre desde el archivo pregunta_nombre.py
edad()

