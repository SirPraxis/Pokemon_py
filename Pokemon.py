#Definición de recursos:

import requests
import random
import time

pokedex = requests.get('http://pokeapi.co/api/v1/pokedex/1/').json()
pokemonlist = []

for pokemon in pokedex['pokemon']:
    pokemonlist.append(pokemon['name'])

pokemonsalvaje = random.choice(pokemonlist)

pika = requests.get('http://pokeapi.co/api/v1/pokemon/pikachu').json()
req = requests.get('http://pokeapi.co/api/v1/pokemon/' + pokemonsalvaje).json()

class Pokemon:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

Pikachu = Pokemon(pika['hp'], pika['attack'])
Oponente = Pokemon(req['hp'], req['attack'])

#Introducción:

print ("\nTú y Pikachu van caminando por el bosque...")
time.sleep(1)
print ("¡cuando un %s salvaje aparece frente a ustedes!\n" % pokemonsalvaje.capitalize())
time.sleep(1)

#Funciones de ataque:

def turnoOponente():
    sel = "a"
    time.sleep(1)
    if sel == 'a':
        Pikachu.hp -= Oponente.atk
        print ("¡%s ha contraatacado!" % pokemonsalvaje.capitalize())
        time.sleep(1)
    else:
        print ("%s se sentó en el suelo a esperar algo..." % pokemonsalvaje.capitalize())
    print ("_____________________________")

def turnoPikachu():
    print ("Pikachu (HP: " + str(Pikachu.hp) + ") / %s (HP: " % pokemonsalvaje.capitalize() + str(Oponente.hp) + ")\n")
    time.sleep(1)
    if choice == 'a':
        Oponente.hp -= Pikachu.atk
        print ("¡El ataque ha surtido efecto!")
        time.sleep(1)
    else:
        print ("Tu Pikachu se sentó en el suelo a esperar algo...")
    print ("_____________________________")

#Bloque de fases:

while Oponente.hp > 0:
    choice = input("Escribe 'a' para atacar o 'e' para esperar: ")
    turnoPikachu()
    if Oponente.hp > 0:
        print ("Pikachu (HP: " + str(Pikachu.hp) + ") / %s (HP: " % pokemonsalvaje.capitalize() + str(Oponente.hp) + ")\n")
        turnoOponente()
        if Pikachu.hp <= 0:
            print ("Pikachu se ha desmayado. \n---GG.\n")
            break
    else:
        print ("K.O.! %s se ha desmayado\n" % pokemonsalvaje.capitalize())
