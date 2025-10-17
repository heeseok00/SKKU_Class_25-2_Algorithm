# Binary Tree Traversal (Divide and Conquer)
# Preorder, Inorder, Postorder 구현

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 전위 순회: Root → Left → Right
def preorder(node):
    if node:
        print(node.key, end=" ")
        preorder(node.left)
        preorder(node.right)


# 중위 순회: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)


# 후위 순회: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=" ")


def main(): #제시된 트리 구조 

    root = Node(60)
    root.left = Node(41)
    root.right = Node(74)

    root.left.left = Node(16)
    root.left.right = Node(53)
    root.right.left = Node(65)

    root.left.left.right = Node(25)
    root.left.right.left = Node(46)
    root.left.right.right = Node(55)

    root.left.right.left.left = Node(42)

    root.right.left.left = Node(63)
    root.right.left.right = Node(70)

    root.right.left.left.left = Node(62)
    root.right.left.left.right = Node(64)

    print("=== Preorder (전위 순회) ===")
    preorder(root)
    print("\n")

    print("=== Inorder (중위 순회) ===")
    inorder(root)
    print("\n")

    print("=== Postorder (후위 순회) ===")
    postorder(root)
    print("\n")


if __name__ == "__main__":
    main()
