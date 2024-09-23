class Node() :

    def __init__(self, data) :
        self.data = data
        self.next = None  #le prochain noeud



class LinkedList() :
    
    def __init__(self) :
        self.head = None  #liste vide


    def printList(self) : 
        """
        Affiche la liste
        """
        liste = self.head
        while liste :
            print(liste.data, end=" -> ")
            liste = liste.next
        print("None")

    
    def printListRec(self, node) :
        """
        Affiche la liste de manière récursive
        """
        if node :
            print(node.data, end=" -> ")
            self.printListRec(node.next)
        else :
            print("None")

    
    def printListRecRev(self, node) : 
        """
        Affiche la liste de manière récursive, mais dans leur ordre inverse
        """
        if node : 
            self.printListRecRev(node.next)
            print(node.data, end=" -> ")
        else :
            print("None")


    def countNodes(self, node) :
        """
        Compte les noeuds de manière récursive
        """
        if not node :
            return 0
        return 1 + self.countNodes(node.next)

    
    def addInHead(self, data) : 
        """
        Ajoute une nouveau noeud en tête de liste avec la valeur de data
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def reverseList(self) :
        """
        Crée une nouvelle liste, mais avec les valeurs inverses
        """

        myLinkedList2 = LinkedList()
        current = self.head
        
        while current is not None:
            myLinkedList2.addInHead(current.data)
            current = current.next
        
        return myLinkedList2


    def addInTail(self, data):
        """Ajoute un nœud à la fin de la liste de manière récursive."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self._addInTailRec(self.head, new_node)

    def _addInTailRec(self, current, new_node):
        if current.next is None:
            current.next = new_node
        else:
            self._addInTailRec(current.next, new_node)


    def addSorted(self, data):
        """Ajoute un nœud dans une liste triée de manière récursive."""
        new_node = Node(data)
        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self._addSortedRec(self.head, new_node)

    def _addSortedRec(self, current, new_node):
        if current is None or current.data >= new_node.data:
            new_node.next = current
            return new_node
        current.next = self._addSortedRec(current.next, new_node)
        return current


    def remove(self, data):
        """Supprime tous les nœuds contenant la valeur 'data' de manière récursive."""
        self.head = self._removeRec(self.head, data)

    def _removeRec(self, current, data):
        if current is None:
            return None
        if current.data == data:
            return self._removeRec(current.next, data)
        else:
            current.next = self._removeRec(current.next, data)
            return current


    def merge(self, autre_liste) :
        """
        Fusionne la liste avec une autre_liste, en les gardant triées
        """
        dummy = Node(0)
        tail = dummy
        list1 = self.head
        list2 = autre_liste.head

        while list1 and list2 : 
            if list1.data <= list2.data :
                tail.next = Node(list1.data)
                list1 = list1.next
            else :
                tail.next = Node(list2.data)
                list2 = list2.next
            tail = tail.next
        
        if list1 :
            tail.next = Node(list1.data)
        if list2 :
            tail.next = Node(list2.data)

        self.head = dummy.next


    def Head(self, N):
        """Retourne une nouvelle liste avec les N premiers éléments de manière récursive."""
        new_list = LinkedList()
        self._HeadRec(self.head, N, new_list)
        return new_list

    def _HeadRec(self, current, N, new_list):
        if current is None or N == 0:
            return
        new_list.addInTail(current.data)
        self._HeadRec(current.next, N - 1, new_list)


    def Tail(self, N):
        """Retourne une nouvelle liste avec les N derniers éléments de manière récursive."""
        total_nodes = self.countNodes(self.head)
        start_index = total_nodes - N
        new_list = LinkedList()
        self._TailRec(self.head, start_index, new_list)
        return new_list

    def _TailRec(self, current, start_index, new_list):
        if current is None:
            return
        if start_index <= 0:
            new_list.addInTail(current.data)
        self._TailRec(current.next, start_index - 1, new_list)


##################################################
#                  Phase de tests                #
##################################################

ll = LinkedList()
ll.addInHead(40)
ll.addInHead(30)
ll.addInHead(20)
ll.addInHead(10)

print("Liste affichée de manière itérative : ")
ll.printList()

print("\n")
print("Liste affichée de manière récursive : ")
ll.printListRec(ll.head)

print("\n")
print("Liste affichée de manière récursive et inversée : ")
ll.printListRecRev(ll.head)

print("\n")
print("Le nombre de noeuds dans la liste : ")
print(ll.countNodes(ll.head))

print("\n")
#print("Crée une nouvelle liste inversée : ")
#reverselist = ll.reverseList()
#reverselist.printListRec()

ll.addInTail(66)
print("Ajoute la valeur à la fin : ")
ll.printList()

print("\n")
ll.addSorted(33)
print("Ajoute la valeur en la triant : ")
ll.printList()

print("\n")
ll.remove(20)
print("Supprime les valeurs 20 : ")
ll.printList()

print("\n")
other_list = LinkedList()
other_list.addInTail(15)
other_list.addInTail(25)
other_list.addInTail(35)
other_list.addInTail(45)
print("Les deux listes avant la fusion : ")
ll.printList()
other_list.printList()
ll.merge(other_list)
print("Fusion avec une autre liste triée : ")
ll.printList()
print("Pas de modification sur l'autre liste : ")
other_list.printList()

print("\n")
head_list = ll.Head(5)
print("Affiche les 5 premiers éléments de la liste : ")
head_list.printList()

print("\n")
tail_list = ll.Tail(5)
print("Affiche les 5 derniers éléments de la liste : ")
tail_list.printList()