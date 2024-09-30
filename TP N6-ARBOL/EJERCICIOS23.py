arbol_criaturas = ArbolBinario()
arbol_criaturas.insertar("Ceto", "Zeus", descripcion="Criatura marina, madre de monstruos marinos.")
arbol_criaturas.insertar("Tifón", "Zeus", descripcion="Gigante monstruoso con cientos de cabezas de dragón.")
arbol_criaturas.insertar("Equidna", "Argos Panoptes", descripcion="Mitad mujer y mitad serpiente, madre de monstruos.")
arbol_criaturas.insertar("Dino", "Atalanta", descripcion="Criatura terrorífica de la mitología griega.")
arbol_criaturas.insertar("Prefredo", "Carcinos", descripcion="Una de las Grayas, hermanas de las Gorgonas.")
arbol_criaturas.insertar("Enio", "Gerión", descripcion="Una de las diosas de la guerra.")
arbol_criaturas.insertar("Escila", None, descripcion="Monstruo marino con cabezas de perro.")
arbol_criaturas.insertar("Caribdis", None, descripcion="Monstruo marino que genera vorágines en el mar.")
arbol_criaturas.insertar("Medusa", "Perseo", descripcion="Gorgona capaz de convertir en piedra con la mirada.")
arbol_criaturas.insertar("Ladón", "Heracles", capturado_por="Heracles", descripcion="Dragón que custodia las manzanas doradas del jardín de las Hespérides.")
arbol_criaturas.insertar("Hidra de Lerna", "Heracles", descripcion="Serpiente monstruosa con múltiples cabezas.")
arbol_criaturas.insertar("Cerbero", "Heracles", capturado_por="Heracles", descripcion="Perro de tres cabezas que guarda el inframundo.")

def listar_inorden_con_derrotador(nodo):
    if nodo:
        listar_inorden_con_derrotador(nodo.izquierdo)
        print(f"Criatura: {nodo.nombre_criatura}, Derrotado por: {nodo.derrotado_por}")
        listar_inorden_con_derrotador(nodo.derecho)

listar_inorden_con_derrotador(arbol_criaturas.raiz)
criatura_talos = arbol_criaturas.buscar("Talos")
if criatura_talos:
    print(f"Criatura: {criatura_talos.nombre_criatura}, Derrotado por: {criatura_talos.derrotado_por}, Descripción: {criatura_talos.descripcion}")
else:
    print("La criatura Talos no fue encontrada.")
from collections import Counter

def contar_derrotadores(nodo, contador):
    if nodo:
        if nodo.derrotado_por:
            contador[nodo.derrotado_por] += 1
        contar_derrotadores(nodo.izquierdo, contador)
        contar_derrotadores(nodo.derecho, contador)

contador_derrotadores = Counter()
contar_derrotadores(arbol_criaturas.raiz, contador_derrotadores)
top_3_derrotadores = contador_derrotadores.most_common(3)

print("Top 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
for derrotador, cantidad in top_3_derrotadores:
    print(f"{derrotador}: {cantidad} criaturas")
def listar_derrotados_por(nodo, heroe):
    if nodo:
        if nodo.derrotado_por == heroe:
            print(nodo.nombre_criatura)
        listar_derrotados_por(nodo.izquierdo, heroe)
        listar_derrotados_por(nodo.derecho, heroe)

print("Criaturas derrotadas por Heracles:")
listar_derrotados_por(arbol_criaturas.raiz, "Heracles")
def listar_no_derrotadas(nodo):
    if nodo:
        if nodo.derrotado_por is None:
            print(nodo.nombre_criatura)
        listar_no_derrotadas(nodo.izquierdo)
        listar_no_derrotadas(nodo.derecho)

print("Criaturas no derrotadas:")
listar_no_derrotadas(arbol_criaturas.raiz)
criaturas_capturadas = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]

for criatura in criaturas_capturadas:
    nodo = arbol_criaturas.buscar(criatura)
    if nodo:
        nodo.capturado_por = "Heracles"
        print(f"{criatura} ha sido capturado por Heracles.")
def buscar_por_coincidencia(nodo, termino):
    if nodo:
        if termino.lower() in nodo.nombre_criatura.lower():
            print(nodo.nombre_criatura)
        buscar_por_coincidencia(nodo.izquierdo, termino)
        buscar_por_coincidencia(nodo.derecho, termino)

buscar_por_coincidencia(arbol_criaturas.raiz, "Cerbero") 
arbol_criaturas.eliminar("Basilisco")
arbol_criaturas.eliminar("Sirenas")
nodo_aves = arbol_criaturas.buscar("Aves del Estínfalo")
if nodo_aves:
    nodo_aves.derrotado_por = "Heracles"
    nodo_aves.descripcion += " Heracles derrotó a varias de ellas."
nodo_ladon = arbol_criaturas.buscar("Ladón")
if nodo_ladon:
    nodo_ladon.nombre_criatura = "Dragón Ladón"
from collections import deque

def listar_por_nivel(raiz):
    if raiz is None:
        return
    cola = deque([raiz])
    while cola:
        nodo = cola.popleft()
        print(nodo.nombre_criatura)
        if nodo.izquierdo:
            cola.append(nodo.izquierdo)
        if nodo.derecho:
            cola.append(nodo.derecho)

listar_por_nivel(arbol_criaturas.raiz)
def listar_capturadas_por_heracles(nodo):
    if nodo:
        if nodo.capturado_por == "Heracles":
            print(nodo.nombre_criatura)
        listar_capturadas_por_heracles(nodo.izquierdo)
        listar_capturadas_por_heracles(nodo.derecho)

print("Criaturas capturadas por Heracles:")
listar_capturadas_por_heracles(arbol_criaturas.raiz)
