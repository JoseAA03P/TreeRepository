class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def es_primo_criba(numero):
    if numero <= 1:
        return False

    # Creamos una lista de booleanos para representar números del 0 al numero dado.
    # Inicializamos todos los elementos como True.
    criba = [True] * (numero + 1)
    criba[0] = criba[1] = False  # 0 y 1 no son primos.

    for p in range(2, int(numero**0.5) + 1):
        if criba[p]:
            # Marcar todos los múltiplos de p como no primos.
            for i in range(p * p, numero + 1, p):
                criba[i] = False

    # Si el número en sí mismo está marcado como primo en la criba, entonces es primo.
    return criba[numero]

def concatenar_rutas_arbol(raiz, ruta_actual="", rutas=[]):
    if raiz is None:
        return

    # Agregar el valor del nodo actual a la ruta actual
    ruta_actual += str(raiz.valor)

    # Si es una hoja, agregar la ruta actual a la lista de rutas
    if raiz.izquierda is None and raiz.derecha is None:
        rutas.append(ruta_actual)
    else:
        # Si no es una hoja, continuar explorando por la izquierda y derecha
        concatenar_rutas_arbol(raiz.izquierda, ruta_actual, rutas)
        concatenar_rutas_arbol(raiz.derecha, ruta_actual, rutas)

# Ejemplo de uso:
# Crear un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Inicializar una lista para almacenar las rutas
rutas = []
rutas_primas = []

# Llamar a la función para concatenar las rutas
concatenar_rutas_arbol(raiz, "", rutas)

# Imprimir las rutas resultantes
for ruta in rutas:
    print(ruta)

#Guardar rutas primas 
for ruta in rutas:
    if es_primo_criba(int(ruta)) == True:
        rutas_primas.append(ruta)

if (len(rutas_primas) > 0):
    print("La ruta prima mas grande es:", max(rutas_primas))

