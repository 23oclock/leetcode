class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def read_tree(nums):
    # nums is level-travered
    nodes = []
    for num in nums:
        nodes.append(TreeNode(num) if num else None)
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[2*i+1] if 2*i+1 < len(nodes) else None
            node.right = nodes[2*i+2] if 2*i+2 < len(nodes) else None
    return nodes[0]


def preorder_traverse_recursive(root):
    def recurse(root):
        if not root:
            return
        nums.append(root.val)
        recurse(root.left)
        recurse(root.right)
    nums = []
    recurse(root)
    return nums


def preorder_traverse(root):
    stack = []
    nums = []
    stack.append(root)
    while stack:
        p = stack.pop()
        if p:
            nums.append(p.val)
            stack.append(p.right)
            stack.append(p.left)
    return nums


def inorder_traverse_recursive(root):
    def recurse(root):
        if not root:
            return
        recurse(root.left)
        nums.append(root.val)
        recurse(root.right)
    nums = []
    recurse(root)
    return nums


def inorder_traverse(root):
    nums = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        p = stack.pop()
        nums.append(p.val)
        curr = p.right
    return nums


def backorder_traverse_recursive(root):
    def recurse(root):
        if not root:
            return
        recurse(root.left)
        recurse(root.right)
        nums.append(root.val)
    nums = []
    recurse(root)
    return nums


def backorder_traverse(root):
    nums = []
    stack = []
    curr = root
    visited = None
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        p = stack.pop()
        if not p.right or p.right == visited:
            nums.append(p.val)
            visited = p
            curr = None
        else:
            stack.append(p)
            curr = p.right
    return nums



if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, None, 6, 7, 8]
    root = read_tree(nums)
    print(preorder_traverse_recursive(root))
    print(preorder_traverse(root))
    print(inorder_traverse_recursive(root))
    print(inorder_traverse(root))
    print(backorder_traverse_recursive(root))
    print(backorder_traverse(root))