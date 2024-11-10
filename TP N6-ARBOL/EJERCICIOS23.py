from collections import Counter, deque

class ArbolBinario:
    class __Node:
        def __init__(self, nombre_criatura, derrotado_por=None, capturado_por=None, descripcion=""):
            self.nombre_criatura = nombre_criatura
            self.derrotado_por = derrotado_por
            self.capturado_por = capturado_por
            self.descripcion = descripcion
            self.izquierdo = None
            self.derecho = None

    def __init__(self):
        self.raiz = None

    def insertar(self, nombre_criatura, derrotado_por=None, capturado_por=None, descripcion=""):
        nuevo_nodo = self.__Node(nombre_criatura, derrotado_por, capturado_por, descripcion)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.nombre_criatura < nodo_actual.nombre_criatura:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def buscar(self, nombre_criatura):
        return self._buscar_recursivo(self.raiz, nombre_criatura)

    def _buscar_recursivo(self, nodo_actual, nombre_criatura):
        if nodo_actual is None:
            return None
        if nodo_actual.nombre_criatura == nombre_criatura:
            return nodo_actual
        elif nombre_criatura < nodo_actual.nombre_criatura:
            return self._buscar_recursivo(nodo_actual.izquierdo, nombre_criatura)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, nombre_criatura)

    def eliminar(self, nombre_criatura):
        # Implementación para eliminar el nodo dado
        pass

    def listar_inorden_con_derrotador(self, nodo):
        if nodo:
            self.listar_inorden_con_derrotador(nodo.izquierdo)
            print(f"Criatura: {nodo.nombre_criatura}, Derrotado por: {nodo.derrotado_por}")
            self.listar_inorden_con_derrotador(nodo.derecho)

    def contar_derrotadores(self, nodo, contador):
        if nodo:
            if nodo.derrotado_por:
                contador[nodo.derrotado_por] += 1
            self.contar_derrotadores(nodo.izquierdo, contador)
            self.contar_derrotadores(nodo.derecho, contador)

    def listar_derrotados_por(self, nodo, heroe):
        if nodo:
            if nodo.derrotado_por == heroe:
                print(nodo.nombre_criatura)
            self.listar_derrotados_por(nodo.izquierdo, heroe)
            self.listar_derrotados_por(nodo.derecho, heroe)

    def listar_no_derrotadas(self, nodo):
        if nodo:
            if nodo.derrotado_por is None:
                print(nodo.nombre_criatura)
            self.listar_no_derrotadas(nodo.izquierdo)
            self.listar_no_derrotadas(nodo.derecho)

    def listar_por_nivel(self):
        if self.raiz is None:
            return
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            print(nodo.nombre_criatura)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

    def listar_capturadas_por_heracles(self, nodo):
        if nodo:
            if nodo.capturado_por == "Heracles":
                print(nodo.nombre_criatura)
            self.listar_capturadas_por_heracles(nodo.izquierdo)
            self.listar_capturadas_por_heracles(nodo.derecho)

    def buscar_por_coincidencia(self, nodo, termino):
        if nodo:
            if termino.lower() in nodo.nombre_criatura.lower():
                print(nodo.nombre_criatura)
            self.buscar_por_coincidencia(nodo.izquierdo, termino)
            self.buscar_por_coincidencia(nodo.derecho, termino)


# Ejemplo de uso
arbol_criaturas = ArbolBinario()
arbol_criaturas.insertar("Ceto", "Zeus", descripcion="Criatura marina, madre de monstruos marinos.")
arbol_criaturas.insertar("Tifón", "Zeus", descripcion="Gigante monstruoso con cientos de cabezas de dragón.")
# (continúa con las demás criaturas...)

# Listar criaturas en orden
arbol_criaturas.listar_inorden_con_derrotador(arbol_criaturas.raiz)

# Top 3 derrotadores
contador_derrotadores = Counter()
arbol_criaturas.contar_derrotadores(arbol_criaturas.raiz, contador_derrotadores)
top_3_derrotadores = contador_derrotadores.most_common(3)
print("Top 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
for derrotador, cantidad in top_3_derrotadores:
    print(f"{derrotador}: {cantidad} criaturas")

# Listar criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles:")
arbol_criaturas.listar_derrotados_por(arbol_criaturas.raiz, "Heracles")

# Listar criaturas no derrotadas
print("Criaturas no derrotadas:")
arbol_criaturas.listar_no_derrotadas(arbol_criaturas.raiz)

# Listar criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles:")
arbol_criaturas.listar_capturadas_por_heracles(arbol_criaturas.raiz)

# Búsqueda por coincidencia de nombre
print("Búsqueda por coincidencia 'Cerbero':")
arbol_criaturas.buscar_por_coincidencia(arbol_criaturas.raiz, "Cerbero")

# Listado por nivel
print("Listado por nivel:")
arbol_criaturas.listar_por_nivel()
