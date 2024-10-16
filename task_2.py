from avl import insert, AVLNode


def find_min_in_tree(node: AVLNode) -> AVLNode:
    if node.left is not None:
        return find_min_in_tree(node.left)

    return node

root = None
keys = [10, 20, 30, 25, 28, 27,  50, 51, 52, 53]

for key in keys:
    root = insert(root, key)

print("AVL-Tree:")
print(root)


print(f'min node: {find_min_in_tree(root).key}')