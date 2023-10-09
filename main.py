class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root, val):
    if root is None:
        return

    queue = []  # Usamos una cola para el recorrido BFS
    queue.append(root)

    while queue:
        node = queue.pop(0)  # Sacamos el primer nodo de la cola
        print(node.value, end=' ')
        if (val == node.value):
            bandera = 1
            return bandera
            break
        # Encolamos los hijos del nodo actual (si existen)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Crear un árbol binario de ejemplo
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

# Ejecutar BFS en el árbol
bandera = 0
val = 100
print("Recorrido BFS:")
bandera = bfs(a, val)

#Se busca un número en el arreglo
print ("")
print("El valor", val)
print("El valor buscado:")
if bandera == 1:
    print("Si esta")
else:
    print("No esta")