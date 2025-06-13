tree = [None, 1,2,3,4,5,6]


def get_children(index):
    left = 2 * index
    right = 2 * index + 1
    return (
        tree[left] if left < len(tree) else None,
        tree[right] if right < len(tree) else None
    )

def get_parent(index):
    if index == 1:
        return None
    return tree[index // 2]

print("2의 자식:", get_children(2))   # (4, 5)
print("3의 자식:", get_children(3))   # (6, None)
print("5의 부모:", get_parent(5))     # 2