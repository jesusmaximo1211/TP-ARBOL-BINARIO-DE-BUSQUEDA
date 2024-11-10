class ArbolPersonajesMCU:
    class __Node:
        def __init__(self, nombre, es_heroe):
            self.nombre = nombre
            self.es_heroe = es_heroe
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insertar(self, nombre, es_heroe):
        self.root = self.__insertar_recursivo(self.root, nombre, es_heroe)

    def __insertar_recursivo(self, nodo, nombre, es_heroe):
        if nodo is None:
            return self.__Node(nombre, es_heroe)
        if nombre < nodo.nombre:
            nodo.left = self.__insertar_recursivo(nodo.left, nombre, es_heroe)
        else:
            nodo.right = self.__insertar_recursivo(nodo.right, nombre, es_heroe)
        return nodo

    def listar_villanos(self):
        villanos = []
        self.__inorden_villanos(self.root, villanos)
        return villanos

    def __inorden_villanos(self, nodo, villanos):
        if nodo:
            self.__inorden_villanos(nodo.left, villanos)
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self.__inorden_villanos(nodo.right, villanos)

    def listar_heroes_con_c(self):
        heroes_c = []
        self.__inorden_heroes_c(self.root, heroes_c)
        return heroes_c

    def __inorden_heroes_c(self, nodo, heroes_c):
        if nodo:
            self.__inorden_heroes_c(nodo.left, heroes_c)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                heroes_c.append(nodo.nombre)
            self.__inorden_heroes_c(nodo.right, heroes_c)

    def contar_heroes(self):
        return self.__contar_heroes_recursivo(self.root)

    def __contar_heroes_recursivo(self, nodo):
        if nodo is None:
            return 0
        count = 1 if nodo.es_heroe else 0
        count += self.__contar_heroes_recursivo(nodo.left)
        count += self.__contar_heroes_recursivo(nodo.right)
        return count

    def corregir_doctor_strange(self):
        nodo = self.__buscar_proximidad(self.root, "Doctor Strange")
        if nodo:
            nodo.nombre = "Doctor Strange"

    def __buscar_proximidad(self, nodo, nombre_objetivo):
        if nodo is None:
            return None
        if nombre_objetivo.lower() in nodo.nombre.lower():
            return nodo
        left_result = self.__buscar_proximidad(nodo.left, nombre_objetivo)
        return left_result if left_result else self.__buscar_proximidad(nodo.right, nombre_objetivo)

    def listar_heroes_descendente(self):
        heroes = []
        self.__postorden_heroes(self.root, heroes)
        return heroes

    def __postorden_heroes(self, nodo, heroes):
        if nodo:
            self.__postorden_heroes(nodo.right, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self.__postorden_heroes(nodo.left, heroes)

    def generar_bosque(self):
        arbol_heroes = ArbolPersonajesMCU()
        arbol_villanos = ArbolPersonajesMCU()
        self.__separar_en_bosque(self.root, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def __separar_en_bosque(self, nodo, arbol_heroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self.__separar_en_bosque(nodo.left, arbol_heroes, arbol_villanos)
            self.__separar_en_bosque(nodo.right, arbol_heroes, arbol_villanos)

    def barrido_alfabetico(self):
        personajes = []
        self.__inorden(self.root, personajes)
        return personajes

    def __inorden(self, nodo, personajes):
        if nodo:
            self.__inorden(nodo.left, personajes)
            personajes.append(nodo.nombre)
            self.__inorden(nodo.right, personajes)

    def contar_nodos(self):
        return self.__contar_nodos_recursivo(self.root)

    def __contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.__contar_nodos_recursivo(nodo.left) + self.__contar_nodos_recursivo(nodo.right)


# Crear el árbol y agregar personajes
arbol = ArbolPersonajesMCU()
arbol.insertar("Iron Man", True)
arbol.insertar("Thanos", False)
arbol.insertar("Captain America", True)
arbol.insertar("Loki", False)
arbol.insertar("Doctor Strnge", True)  # cargado con error a propósito
arbol.insertar("Black Widow", True)
arbol.insertar("Ultron", False)
arbol.insertar("Spider-Man", True)

# b) Listar los villanos ordenados alfabéticamente
villanos_ordenados = arbol.listar_villanos()
print("Villanos ordenados:", villanos_ordenados)

# c) Mostrar los superhéroes que empiezan con "C"
heroes_con_c = arbol.listar_heroes_con_c()
print("Héroes que empiezan con C:", heroes_con_c)

# d) Contar cuántos superhéroes hay en el árbol
total_heroes = arbol.contar_heroes()
print("Total de héroes:", total_heroes)

# e) Corregir el nombre de "Doctor Strange" (cargado como "Doctor Strnge")
arbol.corregir_doctor_strange()
print("Nombre corregido de Doctor Strange en el árbol:", arbol.barrido_alfabetico())

# f) Listar los superhéroes en orden descendente
heroes_descendentes = arbol.listar_heroes_descendente()
print("Héroes en orden descendente:", heroes_descendentes)

# g) Generar un bosque de héroes y villanos
arbol_heroes, arbol_villanos = arbol.generar_bosque()

# g.I) Contar los nodos en cada árbol del bosque
total_heroes_bosque = arbol_heroes.contar_nodos()
total_villanos_bosque = arbol_villanos.contar_nodos()
print("Total de héroes en el bosque:", total_heroes_bosque)
print("Total de villanos en el bosque:", total_villanos_bosque)

# g.II) Barrido ordenado alfabéticamente de cada árbol en el bosque
heroes_bosque_ordenados = arbol_heroes.barrido_alfabetico()
villanos_bosque_ordenados = arbol_villanos.barrido_alfabetico()
print("Héroes en el bosque ordenados alfabéticamente:", heroes_bosque_ordenados)
print("Villanos en el bosque ordenados alfabéticamente:", villanos_bosque_ordenados)


