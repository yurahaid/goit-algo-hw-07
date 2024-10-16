from avl import insert, AVLNode


def sum_tree(node: AVLNode) -> int:
    sum = 0;
    if node.left is not None:
        sum += sum_tree(node.left)

    if node.right is not None:
        sum += sum_tree(node.right)

    return node.key + sum

root = None
keys = [10, 20, 30, 25, 28, 27,  50, 51, 52, 53, -100]

for key in keys:
    root = insert(root, key)


print("AVL-Tree:")
print(root)


print(f'sum all nodes in tree: {sum_tree(root)}')