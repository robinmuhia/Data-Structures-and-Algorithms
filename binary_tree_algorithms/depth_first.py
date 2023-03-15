def depth_first_values(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values