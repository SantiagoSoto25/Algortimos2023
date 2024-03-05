"""5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
(MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""

from arbol_binario import BinaryTree

arbol = BinaryTree()

lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'rhino', 'heroe': False},
    {'name': 'juggernaut', 'heroe': False},
    {'name': 'deadpool', 'heroe': True}
]


for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

# b
arbol.inorden_super_or_villano(False)
print()
# c
arbol.inorden_start_with('C')
print()
# d
print('cantidad de superheroes:', arbol.contar_heroes())
print()
# e
arbol.search_by_coincidence('do')
value = input('ingrese el nombre que desea modificar: ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
print()
arbol.inorden()

# f

arbol.by_level()

# g

superheroes = BinaryTree()
villians = BinaryTree()

arbol.get_heroe_villano(superheroes, villians)
print()
print(f'Los heroes son {superheroes.contar_heroes()}')
print(f'Los villanos son {villians.contar_villians()}')

print()
print('superheroes:')
superheroes.inorden()

print()
print('villians:')
villians.inorden()
print()




