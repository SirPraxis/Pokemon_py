import random
import time

#Fase de eleccion

user = raw_input('Bienvenido a Pokemon Py! \n Elige a Charmander, Squirtle o Bulbasaur: ')
#time.sleep(2)
print "Tu y {} estan caminando por el bosque...".format(user)
#time.sleep(2)
print "cuando un Mewtwo salvaje se aparece frente a ustedes!"

#Fase de ataque

Mewtwo = 500
#time.sleep(3)
print "\n {} VS Mewtwo (PV: {}) \n".format(user, Mewtwo)

ataques_char = {'lanzallamas': 80, 'coletazo': 50}

def ataque(x):
    while Mewtwo > 0:
        x = raw_input("Escribe 'l' para usar lanzallamas o 'c' para usar coletazo")
        if x == "l":
            Mewtwo -= ataques_char['lanzallamas']
        elif x == "c":
            Mewtwo -= ataques_char['coletazo']
    else:
        print "Mataste a Mewtwo"
    return

#Fin del juego
