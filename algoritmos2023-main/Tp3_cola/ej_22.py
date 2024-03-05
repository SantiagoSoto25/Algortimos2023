from cola1 import Cola
        
'''22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
F)por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.'''

personajes = [
    {'nombre':'Steve Rogers','superheroe':'Capitan America','sexo':'M'},
    {'nombre':'Peter Parker','superheroe':'Spider-Man','sexo':'M'},
    {'nombre':'Kate Bishop','superheroe':'Ojo de halcon','sexo':'F'},
    {'nombre':'Carol Danvers','superheroe':'Capitana Marvel','sexo':'F'},
    {'nombre':'stephen Strange','superheroe':'Doctor Strange','sexo':'M'},
    {'nombre':'Scott Lang','superheroe':'Ant-Man','sexo':'M'}
]

cola_personajes = Cola()

#a
nombre_capitana_marvel = None

for personaje in personajes:
    cola_personajes.arrive(personaje)
    if personaje['superheroe'] == 'Capitana Marvel':
        nombre_capitana_marvel = personaje['nombre']
        break

if nombre_capitana_marvel:
    print(f"El nombre del personaje asociado a 'Capitana Marvel' es: {nombre_capitana_marvel}")


#b
for personaje in personajes:
    cola_personajes.arrive(personaje)

print("Nombres de superhéroes femeninos:")
while cola_personajes.size() > 0:
    personaje_actual = cola_personajes.atention()
    if personaje_actual['sexo'] == 'F':
        print(personaje_actual['nombre'])

#c
for personaje in personajes:
    cola_personajes.arrive(personaje)

print("Nombres de superhéroes masculinos:")
while cola_personajes.size() > 0:
    personaje_actual = cola_personajes.atention()
    if personaje_actual['sexo'] == 'M':
        print(personaje_actual['nombre'])

#d
nombre_scott_lang = None

for personaje in personajes:
    cola_personajes.arrive(personaje)
    if personaje['nombre'] == 'Scott Lang':
        nombre_scott_lang = personaje['superheroe']
        break

if nombre_scott_lang:
    print(f"El nombre de superheroe asociado a 'Scott Lang' es: {nombre_scott_lang}")

#e
for personaje in personajes:
    cola_personajes.arrive(personaje)

print("Superhéroes con la letra 'S':")
while cola_personajes.size() > 0:
    personaje_actual = cola_personajes.atention()
    if personaje_actual['nombre'][0].upper() == 'S':
        print(personaje_actual)

#f
nombre_a_buscar = input("Ingrese el nombre del personaje a buscar: ")

personaje_encontrado = None
cola_temporal = Cola()

while cola_personajes.size() > 0:
    personaje_actual = cola_personajes.atention()
    if personaje_actual['nombre'] == nombre_a_buscar:
        personaje_encontrado = personaje_actual
        break
    else:
        cola_temporal.arrive(personaje_actual)

while cola_temporal.size() > 0:
    cola_personajes.arrive(cola_temporal.atention())

if personaje_encontrado:
    print(f"El personaje {nombre_a_buscar} se encuentra en la cola. Su nombre de superhéroe es: {personaje_encontrado['superheroe']}")
else:
    print(f"No se encontró un personaje con el nombre {nombre_a_buscar} en la cola.")
