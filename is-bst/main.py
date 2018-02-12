def check_binary_search_tree_(root):
    def check(root, minx = -2147483648, maxx = 2147483647):
        return root.data > minx and root.data < maxx and (root.left == None or check(root.left, minx, root.data)) and (root.right == None or check(root.right, root.data, maxx))
    return check(root)
