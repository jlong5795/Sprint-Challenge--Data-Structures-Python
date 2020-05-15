class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # self is the root and value is the new one
    def insert(self, value):
        new_node = BSTNode(value)
        # should we go left?
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)
    

    # Return True if the tree contains the value
    # False if it does not
    # When we start self is the root, target is the node
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            # is left a BSTNode?
            if not self.left:
                return False
            # starts the evaluation process again from this node
            return self.left.contains(target)
        else: # if we didn't want to go left, we go right
            # is right a BSTNode?
            if not self.right:
                return False
            # starts the evaluation process again from this node
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current = self.value
        if self.right:
            current = self.right.get_max()
        return current

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the current value
        fn(self.value)
        # if you can pass left, do
        if self.left:
            self.left.for_each(fn)
        # if you can pass right, do
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
           node.left.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            node.right.in_order_print(node.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()

        # passed in node is starting point
        queue.append(node)
        # you have added 1 element to the queue. Print it then pop it off
        while len(queue) > 0:
            print(queue[0].value)
            node = queue.popleft()
        # if it has values it leads to add them to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            print(current.value)