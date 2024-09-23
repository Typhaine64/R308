class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree() :

    def __init__(self) : 
        self.root = None
    

    def printTree(self) :
        """Affiche l'arbre en profondeur (pré-ordre) de manière récursive."""
        self._printTreeRec(self.root)

    def _printTreeRec(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._printTreeRec(node.left)
            self._printTreeRec(node.right)


    def countNodes(self):
        """Retourne le nombre de nœuds dans l'arbre de manière récursive."""
        return self._countNodesRec(self.root)

    def _countNodesRec(self, node):
        if node is None:
            return 0
        return 1 + self._countNodesRec(node.left) + self._countNodesRec(node.right)


    def insert(self, data):
        """Insère une valeur dans l'arbre binaire trié."""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insertRec(self.root, new_node)

    def _insertRec(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insertRec(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insertRec(current.right, new_node)


    def find(self, data):
        """Recherche si une valeur est présente dans l'arbre."""
        return self._findRec(self.root, data)

    def _findRec(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._findRec(node.left, data)
        else:
            return self._findRec(node.right, data)


    def height(self):
        """Calcule la hauteur de l'arbre de manière récursive."""
        return self._heightRec(self.root)

    def _heightRec(self, node):
        if node is None:
            return 0
        left_height = self._heightRec(node.left)
        right_height = self._heightRec(node.right)
        return 1 + max(left_height, right_height)


##################################################
#                  Phase de tests                #
##################################################

# Instanciation de l'arbre
tree = Tree()

# Insertion de valeurs
values = [10, 5, 15, 3, 7, 12, 18]
for value in values:
    tree.insert(value)

# Affichage de l'arbre
print("\n")
print("Affichage de l'arbre (pré-ordre) :")
tree.printTree()

# Compte des nœuds
print("\n")
print("\nNombre de nœuds dans l'arbre :", tree.countNodes())

# Recherche de valeurs
print("\n")
print("Recherche de 7 :", tree.find(7))  # True
print("Recherche de 20 :", tree.find(20))  # False

# Hauteur de l'arbre
print("\n")
print("Hauteur de l'arbre :", tree.height())