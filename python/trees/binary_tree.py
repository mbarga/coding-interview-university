from node import Node
from collections import deque

class Tree:
    root: Node

    def __init__(self, node: Node):
        self.root = node

    def __str__(self):
        output = ""
        for x in self:
            output += f"{str(x)}, "
        return output

    def __iter__(self):
        self.next = self.root
        self.queue = deque([])
        return self
    
    def __next__(self):
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

    def breadth_first_search(self, x):
        for n in self:
            if n.value == x:
                return True
        return False

    def depth_first_search(self, x, node):
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



if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.insert_left(b)
    a.insert_right(c) 
    b.insert_left(d)
    c.insert_right(e)
    t = Tree(a)
    print(t)

    print(t.depth_first_search(4, t.root))
    print("####")
    print(t.depth_first_search(5, t.root))
    # print(t.breadth_first_search(5))
    # print(t.breadth_first_search(6))