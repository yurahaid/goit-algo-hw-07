from avl import insert, AVLNode


def find_max_in_tree(node: AVLNode) -> AVLNode:
    if node.right is not None:
        return find_max_in_tree(node.right)

    return node

root = None
keys = [10, 20, 30, 25, 28, 27, -1, 50, 51, 52, 53]

for key in keys:
    root = insert(root, key)

print("AVL-Tree:")
print(root)


print(f'max node: {find_max_in_tree(root).key}')