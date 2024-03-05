class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

'''24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.'''

pila_personajes = Pila()
pila_personajes.apilar(Personaje('Iron Man', 10))
pila_personajes.apilar(Personaje('Black Widow', 7))
pila_personajes.apilar(Personaje('Groot', 6))
pila_personajes.apilar(Personaje('Spiderman', 7))
pila_personajes.apilar(Personaje('Rocket Raccoon', 7))
pila_personajes.apilar(Personaje('Falcon', 6))

posicion = 1
while not pila_personajes.esta_vacia():
    personaje = pila_personajes.desapilar()
    if personaje.nombre == 'Rocket Raccoon' or personaje.nombre == 'Groot':
        print(f'{personaje.nombre} está en la posición {posicion}')
        break
    posicion += 1

for personaje in pila_personajes.items:
    if personaje.peliculas > 5:
        print(f'{personaje.nombre} aparece en {personaje.peliculas} películas')

for personaje in pila_personajes.items:
    if personaje.nombre == 'Black Widow':
        print(f'{personaje.nombre} aparece en {personaje.peliculas} películas')

for personaje in pila_personajes.items:
    if personaje.nombre.startswith(('C', 'D', 'G')):
        print(personaje.nombre)
