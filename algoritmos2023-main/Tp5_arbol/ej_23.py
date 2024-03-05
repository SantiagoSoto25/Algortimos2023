from arbol_binario import BinaryTree

# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;#?Listo
# b. se debe permitir cargar una breve descripción sobre cada criatura;#?Listo
# c. mostrar toda la información de la criatura Talos;#?Listo
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;#!Falta
# e. listar las criaturas derrotadas por Heracles;#?Listo
# f. listar las criaturas que no han sido derrotadas;#?Listo
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;#?Listo
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;#!Falta
# i. se debe permitir búsquedas por coincidencia;#!?Listo
# j. eliminar al Basilisco y a las Sirenas;#?Listo
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;#!Falta
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;#!Falta
# m. realizar un listado por nivel del árbol;#?Listo
# n. muestre las criaturas capturadas por Heracles.#?Listo

lista_criaturas = [
    {'Criatura': 'Ceto', 'Derrotado': None},
    {'Criatura': 'Tifón', 'Derrotado': 'Zeus'},
    {'Criatura': 'Equidna', 'Derrotado': 'Argos Panoptes'},
    {'Criatura': 'Dino', 'Derrotado': None},
    {'Criatura': 'Pefredo', 'Derrotado': None},
    {'Criatura': 'Enio', 'Derrotado': None},
    {'Criatura': 'Escila', 'Derrotado': None},
    {'Criatura': 'Caribdis', 'Derrotado': None},
    {'Criatura': 'Euríale', 'Derrotado': None},
    {'Criatura': 'Esteno', 'Derrotado': None},
    {'Criatura': 'Medusa', 'Derrotado': 'Perseo'},
    {'Criatura': 'Ladón', 'Derrotado': 'Heracles'},
    {'Criatura': 'Águila del Cáucaso', 'Derrotado': None},
    {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte'},
    {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles'},
    {'Criatura': 'León de Nemea', 'Derrotado': 'Heracles'},
    {'Criatura': 'Esfinge', 'Derrotado': 'Edipo'},
    {'Criatura': 'Dragón de la Cólquida', 'Derrotado': None},
    {'Criatura': 'Cerbero', 'Derrotado': None},
    {'Criatura': 'Cerda de Cromión', 'Derrotado': 'Teseo'},
    {'Criatura': 'Ortro', 'Derrotado': 'Heracles'},
    {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Jabalí de Calidón', 'Derrotado': 'Atalanta'},
    {'Criatura': 'Carcinos', 'Derrotado': None},
    {'Criatura': 'Gerión', 'Derrotado': 'Heracles'},
    {'Criatura': 'Láquesis', 'Derrotado': None},
    {'Criatura': 'Átropos', 'Derrotado': None},
    {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Harpías', 'Derrotado': None},
    {'Criatura': 'Argos Panoptes', 'Derrotado': 'Hermes'},
    {'Criatura': 'Aves del Estínfalo', 'Derrotado': None},
    {'Criatura': 'Talos', 'Derrotado': 'Medea'},
    {'Criatura': 'Sirenas', 'Derrotado': None},
    {'Criatura': 'Pitón', 'Derrotado': 'Apolo'},
    {'Criatura': 'Cierva de Cerinea', 'Derrotado': None},
    {'Criatura': 'Basilisco', 'Derrotado': None},
    {'Criatura': 'Jabali de Erimanto', 'Derrotado': None},
    {'Criatura': 'Cloto', 'Derrotado': None},
]





criaturas_tree = BinaryTree()
for criatura in lista_criaturas:
    criaturas_tree.insert_node(criatura['Criatura'], {'Derrotado': criatura['Derrotado']})

#a
criaturas_tree.inorden_otherValues()
print()

#b
criaturas_tree.inorden_add_field('Descripcion', '-')
criaturas_tree.inorden_otherValues()

#c
bus = criaturas_tree.search('Talos')
if bus is not None:
    print ('La información de Talos es: ', bus.value, bus.other_values)
else:
    print ('Talos no se encuentra en el arbol.')
print()

#d
dic_ranking = {}
criaturas_tree.inorden_ranking(dic_ranking)

def order_por(item):
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print('El TOP 3  de los que han derrotado a más criaturas es: ')
print(ordenados[:3])
print()

#e
print('Las criaturas derrotas por Heracles son: ')
criaturas_tree.inorden_defeats('Heracles')
print()

#f
print('Las criaturas que aún no han sido derrotadas son: ')
criaturas_tree.inorden_defeats(None)
print()

#g
criaturas_tree.inorden_add_field('Capturada', None)
criaturas_tree.inorden_otherValues()
print()

#h
H = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabali de Erimanto']
criaturas_tree.inorden_modify_fields(H, 'Capturada', 'Heracles')
criaturas_tree.inorden_otherValues()
print()

#j
A = 'Basilisco'
B = 'Sirenas'
pos = criaturas_tree.search(A)
if pos:
    criaturas_tree.delete_node(A)
    print(f'{A} se ha eliminado correctamente.')
else:
    print(f'{A} no se encuentra en el arbol.')
print()

pos = criaturas_tree.search(B)
if pos:
    criaturas_tree.delete_node(B)
    print(f'{B} se ha eliminado correctamente.')
else:
    print(f'{B} no se encuentra en el arbol.')
print()

#k
K = ['Aves del Estínfalo']
criaturas_tree.inorden_modify_fields(K, 'Derrotado', 'Heracles')
criaturas_tree.inorden_otherValues()
print()

#l
C = 'Ladón'
pos = criaturas_tree.search(C)
if pos is not None:
    buscado_values = pos.other_values
    criaturas_tree.delete_node(C)
    criaturas_tree.insert_node('Dragón Ladón', buscado_values)
criaturas_tree.inorden_otherValues()
print()

#m
print('Listado por nivel: ')
criaturas_tree.by_level_otherValues()
print()

#n
print('Heracles capturo a:')
criaturas_tree.inorden_capture('Heracles')
print()
