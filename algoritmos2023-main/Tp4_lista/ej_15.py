'''15 Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;'''

from lista2 import Lista

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemones):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemones = pokemones


lista_entrenadores = Lista()


entrenador1 = Entrenador('Ash', 5, 10, 20, [['Bulbasaur', 25, 'Planta', None], ['Pikachu', 30, 'Eléctrico', None]])
entrenador2 = Entrenador('Misty', 3, 5, 15, [['Squirtle', 28, 'Agua', None], ['Charizard', 50, 'Fuego', 'Volador']])


lista_entrenadores.insert(entrenador1)
lista_entrenadores.insert(entrenador2)

#a Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemones(entrenador_nombre):
    entrenador = lista_entrenadores.get_element_by_index(lista_entrenadores.search(entrenador_nombre))
    if entrenador:
        return len(entrenador.pokemones)
    return 0

#b Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos():
    resultado = []
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        if entrenador.torneos_ganados > 3:
            resultado.append(entrenador.nombre)
    return resultado

#c El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel():
    max_torneos = -1
    max_torneos_entrenador = None
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        if entrenador.torneos_ganados > max_torneos:
            max_torneos = entrenador.torneos_ganados
            max_torneos_entrenador = entrenador

    if max_torneos_entrenador:
        max_nivel_pokemon = -1
        max_nivel_pokemon_obj = None
        for pokemon in max_torneos_entrenador.pokemones:
            if pokemon.nivel > max_nivel_pokemon:
                max_nivel_pokemon = pokemon.nivel
                max_nivel_pokemon_obj = pokemon
        return max_nivel_pokemon_obj

#d Mostrar todos los datos de un entrenador y sus Pokémos
def datos_entrenador_y_pokemones(entrenador_nombre):
    entrenador = lista_entrenadores.get_element_by_index(lista_entrenadores.search(entrenador_nombre))
    if entrenador:
        print(f'Entrenador: {entrenador.nombre}')
        print(f'Torneos ganados: {entrenador.torneos_ganados}')
        print(f'Batallas perdidas: {entrenador.batallas_perdidas}')
        print(f'Batallas ganadas: {entrenador.batallas_ganadas}')
        print('Pokémons:')
        for pokemon in entrenador.pokemones:
            print(f'Nombre: {pokemon.nombre}, Nivel: {pokemon.nivel}, Tipo: {pokemon.tipo}, Subtipo: {pokemon.subtipo}')
    else:
        print('Entrenador no encontrado')

#e Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%
def entrenadores_porcentaje_batallas():
    resultado = []
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        porcentaje_ganadas = (entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas)) * 100
        if porcentaje_ganadas > 79:
            resultado.append(entrenador.nombre)
    return resultado

#f Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
def entrenadores_tipo_subtipo(tipo, subtipo):
    resultado = []
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        tiene_tipo_subtipo = any(pokemon.tipo == tipo and pokemon.subtipo == subtipo for pokemon in entrenador.pokemones)
        if tiene_tipo_subtipo:
            resultado.append(entrenador.nombre)
    return resultado

#g El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(entrenador_nombre):
    entrenador = lista_entrenadores.get_element_by_index(lista_entrenadores.search(entrenador_nombre))
    if entrenador:
        total_niveles = sum(pokemon.nivel for pokemon in entrenador.pokemones)
        return total_niveles / len(entrenador.pokemones)
    return 0

#h Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(pokemon_nombre):
    contador = 0
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        tiene_pokemon = any(pokemon.nombre == pokemon_nombre for pokemon in entrenador.pokemones)
        if tiene_pokemon:
            contador += 1
    return contador

#i Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemones_repetidos():
    resultado = []
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        nombres_pokemones = [pokemon.nombre for pokemon in entrenador.pokemones]
        tiene_repetidos = len(nombres_pokemones) != len(set(nombres_pokemones))
        if tiene_repetidos:
            resultado.append(entrenador.nombre)
    return resultado

#j Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemones_especificos(pokemon_lista):
    resultado = []
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        tiene_pokemon = any(pokemon.nombre in pokemon_lista for pokemon in entrenador.pokemones)
       
#k Determinar si un entrenador “X” tiene al Pokémon “Y”
def tiene_entrenador_pokemon(entrenador_nombre, pokemon_nombre):
    entrenador = lista_entrenadores.get_element_by_index(lista_entrenadores.search(entrenador_nombre))
    if entrenador:
        tiene_pokemon = any(pokemon.nombre == pokemon_nombre for pokemon in entrenador.pokemones)
        if tiene_pokemon:
            print(f'El entrenador {entrenador.nombre} tiene al Pokémon {pokemon_nombre}')
            print('Datos del Pokémon:')
            for pokemon in entrenador.pokemones:
                if pokemon.nombre == pokemon_nombre:
                    print(f'Nombre: {pokemon.nombre}, Nivel: {pokemon.nivel}, Tipo: {pokemon.tipo}, Subtipo: {pokemon.subtipo}')
            return True
    print(f'El entrenador {entrenador_nombre} no tiene al Pokémon {pokemon_nombre}')
    return False


print('Cantidad de Pokémons de Ash:', cantidad_pokemones('Ash'))
print('Entrenadores con más de tres torneos ganados:', entrenadores_mas_de_tres_torneos())
print('Pokémon de mayor nivel del entrenador con más torneos ganados:', pokemon_mayor_nivel().nombre)
datos_entrenador_y_pokemones('Misty')
print('Entrenadores con más del 79% de batallas ganadas:', entrenadores_porcentaje_batallas())
print('Entrenadores con Pokémon de tipo Fuego y subtipo Planta o Agua/Volador:', entrenadores_tipo_subtipo('Fuego', 'Planta'))
print('Promedio de nivel de los Pokémons de Ash:', promedio_nivel('Ash'))
print('Cantidad de entrenadores con el Pokémon Charmander:', cantidad_entrenadores_con_pokemon('Charmander'))
print('Entrenadores con Pokémons repetidos:', entrenadores_con_pokemones_repetidos())
print('Entrenadores con los Pokémons Tyrantrum, Terrakion o Wingull:', entrenadores_con_pokemones_especificos(['Tyrantrum', 'Terrakion', 'Wingull']))
tiene_entrenador_pokemon('Ash', 'Pikachu')
tiene_entrenador_pokemon('Misty', 'Pikachu')
