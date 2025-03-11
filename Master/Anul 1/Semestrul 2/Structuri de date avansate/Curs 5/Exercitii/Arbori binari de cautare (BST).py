import random

# key = valoarea dintr-un nod
# left = referinta fiului stang
# right = referinta fiului drept
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# functie care insereaza un nod nou cu cheia "new_key"
# in BST-ul cu radacina "root"
def insertNodeBST(root, new_key):
    if root is None:
        root = TreeNode(new_key)
    else:
        if new_key < root.key:
            root.left = insertNodeBST(root.left, new_key)
        else:
            root.right = insertNodeBST(root.right, new_key)

    return root


# functie care cauta un nod cu cheia "search_key"
# in BST-ul cu radacina "root"
def searchNodeBST(root, search_key):
    if root is None:
        return False
    else:
        if root.key == search_key:
            return True
        else:
            if search_key < root.key:
                return searchNodeBST(root.left, search_key)
            else:
                return searchNodeBST(root.right, search_key)

    return root

# functie care afiseaza parcurgerea in inordine (S-R-D)
# a unui BST cu radacina "root"
def printInorderBST(root):
    if root is not None:
        printInorderBST(root.left)
        print(root.key, end=" ")
        printInorderBST(root.right)


# functie care sterge nodul cu cheia "key" din BST
def deleteNodeBST(root, delete_key):
    if root is None:
        return None

    # caut nodul cu valoarea "key" in BST
    if delete_key < root.key:
        root.left = deleteNodeBST(root.left, delete_key)
        return root
    if delete_key > root.key:
        root.right = deleteNodeBST(root.right, delete_key)
        return root

    # nodul pe care trebuie sa-l stergem nu are nici un fiu,
    # deci el devine direct None
    if root.left is None and root.right is None:
        return None

    # nodul pe care trebuie sa-l stergem are doar fiu drept,
    # deci il inlocuim cu el
    if root.left is None:
        return root.right

    # nodul pe care trebuie sa-l stergem are doar fiu stang,
    # deci il inlocuim cu el
    if root.right is None:
        return root.left

    # nodul pe care trebuie sa-l stergem are si fiu stang si fiu drept

    # cautam succesorul in inordine al nodului pe care dorim sa-l stergem,
    # adica valoarea minima din subarborele sau drept
    succ = root.right
    while succ.left is not None:
        succ = succ.left

    # inlocuim valorea din nodul pe care trebuie sa-l stergem
    # cu succesorul sau in inordine
    root.key = succ.key

    # stergem succesorul in inordine din subarborele drept al nodului
    # pe care trebuie sa-l stergem
    root.right = deleteNodeBST(root.right, root.key)

    return root


# initial, arborele este vid, respectiv radacina "r" este None
r = None
# adaugam n valori aleatorii in BST
n = 20
for k in range(n):
    x = random.randrange(1, 20)
    r = insertNodeBST(r, x)


print("Parcurgerea in inordine a BST-ului:")
printInorderBST(r)

valoare_cautata = 10
gasit = searchNodeBST(r, valoare_cautata)
print(f"\nValoarea {valoare_cautata} se gaseste in BST!" if gasit
      else f"\nValoarea {valoare_cautata} nu se gaseste in BST!")

r = deleteNodeBST(r, valoare_cautata)
print(f"\nBST-ul dupa stergerea nodului cu valoarea {valoare_cautata}")
printInorderBST(r)

