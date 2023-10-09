class TreeNode:
    def __init__(self, value):
        self.valor = value
        self.derecha = None
        self.izquierda = None

def recorrido_in_order(raiz, matriz):
    if raiz:
        # Recorremos el subárbol izquierdo
        recorrido_in_order(raiz.izquierda, matriz)
        
        # Agregamos el valor del nodo actual a la matriz
        matriz.append(raiz.valor)
        
        # Recorremos el subárbol derecho
        recorrido_in_order(raiz.derecha, matriz)
    

# Crear un árbol binario de ejemplo
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.izquierda = b
a.derecha = c
b.izquierda = d
b.derecha = e
c.izquierda = f
c.derecha = g

# Inicializamos una matriz vacía para almacenar los valores
valores_arbol = []

# Realizamos el recorrido en orden y almacenamos los valores en la matriz
recorrido_in_order(a, valores_arbol)

# Imprimimos la matriz con los valores del árbol
print(valores_arbol)

# Inicializar una variable para la suma
suma = 0

# Recorrer el arreglo y sumar los elementos
for elemento in valores_arbol:
    suma += elemento
    
print("")
print("La suma total del árbol es ", suma)
print("El valor mínimo del árbol es ", min(valores_arbol))

