from grafo2 import Grafo

#15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
#y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#uno en las naturales) y tipo (natural o arquitectónica);
#b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
#la distancia que las separa;
#c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;
#f. deberá utilizar un grafo no dirigido.

mi_grafo = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'

mi_grafo.insert_vertice(Maravilla('Gran Muralla', 'China', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('Machu Picchu', 'Peru', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('Cataratas del Iguazu', 'Argentina', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('Cristo Redentor', 'Brasil', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('Chichén Itzá', 'México', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('Coliseo Romano', 'Italia', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('La Gran Barrera de Coral', 'Australia', 'Natural'), criterio='nombre')

mi_grafo.insert_arist('Gran Muralla', 'Machu Picchu', 100)
mi_grafo.insert_arist('Gran Muralla', 'Petra', 200)
mi_grafo.insert_arist('Gran Muralla', 'Cristo Redentor', 300)
mi_grafo.insert_arist('Gran Muralla', 'Chichén Itzá', 400)
mi_grafo.insert_arist('Gran Muralla', 'Coliseo Romano', 500)
mi_grafo.insert_arist('Machu Picchu', 'Cristo Redentor', 250)
mi_grafo.insert_arist('Machu Picchu', 'Chichén Itzá', 350)
mi_grafo.insert_arist('Machu Picchu', 'Coliseo Romano', 450)
mi_grafo.insert_arist('Cristo Redentor', 'Chichén Itzá', 100)
mi_grafo.insert_arist('Cristo Redentor', 'Coliseo Romano', 200)
mi_grafo.insert_arist('Chichén Itzá', 'Coliseo Romano', 100)
mi_grafo.insert_arist('La Gran Barrera de Coral', 'Cataratas del Iguazu', 200)


ori = 'Gran Muralla'
des = 'Machu Picchu'
origen = mi_grafo.search_vertice(ori, criterio='nombre')
destino = mi_grafo.search_vertice(des, criterio='nombre')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(mi_grafo.has_path(ori, des, criterio='nombre')):
        camino_mas_corto = mi_grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]
a = input()

bosque = mi_grafo.kruskal()
for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

def paises_con_maravillas_arquitectonicas_y_naturales(grafo):
    paises_arquitectonicas = set()
    paises_naturales = set()

    for vertice in grafo._Grafo__elements:
        maravilla = vertice[0]
        pais = maravilla.pais

        if maravilla.tipo == 'Arquitectonica':
            paises_arquitectonicas.add(pais)
        elif maravilla.tipo == 'Natural':
            paises_naturales.add(pais)

    paises_con_ambos_tipos = paises_arquitectonicas.intersection(paises_naturales)

    return paises_con_ambos_tipos

paises_con_maravillas = paises_con_maravillas_arquitectonicas_y_naturales(mi_grafo)

for pais in paises_con_maravillas:
    print(f"{pais} tiene maravillas arquitectónicas y naturales.")

resultado = mi_grafo.paises_maravilla_mismo_tipo()

if resultado:
    print("Sí, hay países con más de una maravilla del mismo tipo.")
else:
    print("No, no hay países con más de una maravilla del mismo tipo.")

