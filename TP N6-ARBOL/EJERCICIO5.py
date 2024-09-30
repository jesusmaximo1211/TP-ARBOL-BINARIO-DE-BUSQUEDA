class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = NodoArbol(nombre, es_heroe)
        else:
            self._insertar_recursivo(self.raiz, nombre, es_heroe)

    def _insertar_recursivo(self, nodo_actual, nombre, es_heroe):
        if nombre < nodo_actual.nombre:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nombre, es_heroe)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo_actual.derecho, nombre, es_heroe)

arbol_mcu = ArbolBinario()

arbol_mcu.insertar("Iron Man", True)
arbol_mcu.insertar("Captain America", True)
arbol_mcu.insertar("Thor", True)
arbol_mcu.insertar("Hulk", True)
arbol_mcu.insertar("Black Widow", True)
arbol_mcu.insertar("Spider-Man", True)
arbol_mcu.insertar("Doctor Strange", True)
arbol_mcu.insertar("Black Panther", True)
arbol_mcu.insertar("Captain Marvel", True)

arbol_mcu.insertar("Thanos", False)
arbol_mcu.insertar("Loki", False)
arbol_mcu.insertar("Ultron", False)
arbol_mcu.insertar("Hela", False)
arbol_mcu.insertar("Red Skull", False)
arbol_mcu.insertar("Killmonger", False)
arbol_mcu.insertar("Mysterio", False)
arbol_mcu.insertar("Vulture", False)


def listar_villanos_inorden(nodo):
    if nodo is not None:
        listar_villanos_inorden(nodo.izquierdo)
        if not nodo.es_heroe:
            print(nodo.nombre)
        listar_villanos_inorden(nodo.derecho)
        
def listar_superheroes_con_C(nodo):
    if nodo is not None:
        listar_superheroes_con_C(nodo.izquierdo)
        if nodo.es_heroe and nodo.nombre.startswith("C"):
            print(nodo.nombre)
        listar_superheroes_con_C(nodo.derecho)

def contar_superheroes(nodo):
    if nodo is None:
        return 0
    conteo = contar_superheroes(nodo.izquierdo) + contar_superheroes(nodo.derecho)
    if nodo.es_heroe:
        conteo += 1
    return conteo

def buscar_proximidad(nodo, nombre_incorrecto, nuevo_nombre):
    if nodo is None:
        return
    if nombre_incorrecto in nodo.nombre:
        print(f"Modificando nombre de {nodo.nombre} a {nuevo_nombre}")
        nodo.nombre = nuevo_nombre
    buscar_proximidad(nodo.izquierdo, nombre_incorrecto, nuevo_nombre)
    buscar_proximidad(nodo.derecho, nombre_incorrecto, nuevo_nombre)

def listar_superheroes_descendente(nodo):
    if nodo is not None:
        listar_superheroes_descendente(nodo.derecho)
        if nodo.es_heroe:
            print(nodo.nombre)
        listar_superheroes_descendente(nodo.izquierdo)

def generar_bosque(nodo, arbol_heroes, arbol_villanos):
    if nodo is not None:
        if nodo.es_heroe:
            arbol_heroes.insertar(nodo.nombre, True)
        else:
            arbol_villanos.insertar(nodo.nombre, False)
        generar_bosque(nodo.izquierdo, arbol_heroes, arbol_villanos)
        generar_bosque(nodo.derecho, arbol_heroes, arbol_villanos)

def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izquierdo) + contar_nodos(nodo.derecho)

def barrido_inorden(nodo):
    if nodo is not None:
        barrido_inorden(nodo.izquierdo)
        print(nodo.nombre)
        barrido_inorden(nodo.derecho)


