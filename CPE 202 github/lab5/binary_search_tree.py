from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        # key is like the index
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        if not self.root:
            return True
        return False

    def search_helper(self, key, node: TreeNode):
        if node is None:
            return False
        elif node.right is None and node.left is None:
            return node.key == key
        elif key == node.key:
            return True
        elif key < node.key:
            return self.search_helper(key, node.left)
        else:
            return self.search_helper(key, node.right)

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.search_helper(key, self.root)

    def insert_helper(self, key, data, node: TreeNode):
        if self.is_empty():
            self.root = TreeNode(key, data)
            return
        elif key == node.key:
            node.data = data
            return
        elif node.right is None and node.key < key:
            node.right = TreeNode(key, data)
            return
        elif node.left is None and node.key > key:
            node.left = TreeNode(key, data)
            return
        elif key < node.key:
            return self.insert_helper(key, data, node.left)
        else:
            return self.insert_helper(key, data, node.right)

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.insert_helper(key, data, self.root)

    def find_min_helper(self, node: TreeNode):
        if node.left == None:
            min_key = node.key
            min_data = node.data
            return (min_key, min_data)
        else:
            return self.find_min_helper(node.left)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_min_helper(self.root)

    def find_max_helper(self, node: TreeNode):
        if node.right == None:
            max_key = node.key
            max_data = node.data
            return (max_key, max_data)
        else:
            return self.find_max_helper(node.right)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)

    def tree_height_helper(self, node: TreeNode):
        if node == None:
            return -1
        left = self.tree_height_helper(node.left)
        right = self.tree_height_helper(node.right)
        return max(left, right) + 1

    def tree_height(self):  # return the height of the tree
        return self.tree_height_helper(self.root)

    def inorder_list_helper(self, node: TreeNode):
        if node is None:
            return []
        left_list = self.inorder_list_helper(node.left)
        right_list = self.inorder_list_helper(node.right)
        return left_list + [node.key] + right_list

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.inorder_list_helper(self.root)

    def preorder_list_helper(self, node: TreeNode):
        # algorithm: root left right
        if node is None:
            return []
        left_list = self.preorder_list_helper(node.left)
        right_list = self.preorder_list_helper(node.right)
        return [node.key] + left_list + right_list

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.preorder_list_helper(self.root)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        if self.is_empty():
            return []
        newL = []
        q = Queue(25000)  # Don't change this!
        # newL.append(self.root.key)
        q.enqueue(self.root)
        while q.size() > 0:
            node = q.dequeue()
            newL.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return newL