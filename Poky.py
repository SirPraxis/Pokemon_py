import random
import time

#Fase de eleccion

pokemon = {'Charmander': {'Lanzallamas': 80, 'Coletazo': 50, 'Torbellino de fuego': 150}, 'Squirtle': {'Chorro de agua': 80, 'Zarpazo': 50, 'Marea alta': 150}, 'Bulbasaur': {'Latico cepa': 80, 'Tacleada': 50, 'Rayo solar': 150}}

user = raw_input('Bienvenido a Pokemon Py! \n Elige a Charmander, Squirtle o Bulbasaur: ')
chosen_powers = pokemon.get(user.capitalize())
#time.sleep(2)
print "Tu y {} estan caminando por el bosque...".format(user)
#time.sleep(2)
print "cuando un Mewtwo salvaje se aparece frente a ustedes!"

#Fase de ataque

#time.sleep(3)

print "\n {} VS Mewtwo (PV: 300)\n".format(user.capitalize())

print "\n Estos son los ataques de tu pokemon: \n {}".format(chosen_powers)

print chosen_powers['1']

Mewtwo = 300

# while Mewtwo > 50:
#     ataque = raw_input("Escribe 1 para usar {}, 2 para usar {} o 3 para usar {}:  ").format()
#     if ataque == '1':
#         Mewtwo -= selection['Lanzallamas']
#         print Mewtwo
#     elif ataque == '2':
#         Mewtwo -= selection['Coletazo']
#         print Mewtwo
#     elif ataque == '3':
#         Mewtwo -= selection['Torbellino de fuego']
#         print Mewtwo
#     else:
#         print "Tu pokemon no conoce ese poder :/ intenta de nuevo... \n"






#         print "Mewtwo rechaza tu pokebola de un coletazo!"
#     elif Mewtwo < 50:
#         print "Has capturado a Mewtwo, felicidades!!!!"
# else:
#     print "Balbuceaste algo? Elige de nuevo tu accion"


# choice = raw_input("Escribe 'a' para atacarlo o 'c' para intentar capturarlo: ")
#
