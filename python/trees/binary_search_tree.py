from node import Node
from collections import deque

class Tree:
    root: Node

    def __init__(self, node: Node = None) -> None:
        self.root = node

    def __len__(self) -> int:
        cnt = 0
        for x in self:
            cnt += 1
        return cnt

    def __str__(self) -> str:
        output = ""
        for x in self:
            output += f"{str(x)}, "
        return output

    def __iter__(self) -> "Tree":
        self.next = self.root
        self.queue = deque([])
        return self
    
    def __next__(self) -> Node:
        # BFS traversal
        if self.next:
            cur = self.next
            if cur.left:
                self.queue.append(cur.left)
            if cur.right:
                self.queue.append(cur.right)
            self.next = self.queue.popleft() if self.queue else None
            return cur 
        else:
            raise StopIteration

    def breadth_first_search(self, x) -> bool:
        for n in self:
            if n.value == x:
                return True
        return False

    def depth_first_search(self, x, node) -> bool:
        if node is None:
            return
        else:
            print(f"found {node.value}")
            if node.value == x:
                return True
            print("search left")
            if self.depth_first_search(x, node.left):
                return True
            print("search right")
            if self.depth_first_search(x, node.right):
                return True
            return False

    @staticmethod
    def min(n: Node) -> Node:
        while n is not None:
            if n.left is None:
                break
            else:
                n = n.left
        return n

    @staticmethod
    def max(n: Node) -> Node:
        while n is not None:
            if n.right is None:
                break
            else:
                n = n.right
        return n 

    def ordered_insert(self, value) -> Node:
        nn = Node(value)
        if self.root:
            cur = self.root
            while True:
                if value < cur.value:
                    if cur.left:
                        cur = cur.left
                    else:
                        nn.parent = cur
                        cur.left = nn
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        nn.parent = cur
                        cur.right = nn
                        break
        else:
            self.root = nn
        return nn

    # NOTE was difficult
    def delete_value(self, x: int, n: Node) -> bool:
        if n is None:
            return 
        if n.value == x:
            #1. leaf node
            #2. one child
            if n.left is None:
                n = n.right
            if n.right is None:
                n = n.left
            #3. two children
            succ = Tree.get_successor(n)
            n = succ
            succ = None
            return True
        elif x < n.value:
            return self.delete_value(x, n.left)
        elif x > n.value:
            return self.delete_value(x, n.right)
        return False

    @staticmethod
    def get_successor(n: Node) -> Node:
        # next highest value in the subtree 
        if n.right is not None:
            n = Tree.min(n.right)
        # travel up the tree until you find a node that is the left child of its parent
        else:
            while n.parent:
                ancestor = n.parent
                if ancestor.left == n:
                    n = ancestor
                    break
                else:
                    n = ancestor
        return n

    # NOTE was difficult
    def get_height(self, node: Node) -> int:
        # find the max depth using a DFS
        if node is None:
            return 0
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1


if __name__ == "__main__":
    t = Tree()
    a = t.ordered_insert(20)
    b = t.ordered_insert(8)
    c = t.ordered_insert(22)
    d = t.ordered_insert(4)
    e = t.ordered_insert(12)
    f = t.ordered_insert(10)
    g = t.ordered_insert(14)
    print(t)
    # print(f"len: {len(t)}")
    # print(f"min: {Tree.min(t.root)}")
    # print(f"max: {Tree.max(t.root)}")
    # print(f"height: {t.get_height(t.root)}")
    # print(f"successor of {g.value} is {Tree.get_successor(g)}")
    print("deleting 14")
    print(t.delete_value(14, t.root))
    print(t)
    print("deleting 22")
    print(t.delete_value(22, t.root))
    print(t)