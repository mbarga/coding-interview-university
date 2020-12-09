
class Node:
    value: int
    left: 'Node'  # forward reference typing
    right: 'Node'  # forward reference typing

    def __init__(self, value: int = None, left = None, right = None, parent = None) -> None:
        self.value = value
        self.left = left
        self.right = right 
        self.parent = parent 

    def __str__(self) -> str:
        return str(self.value)

    def insert_right(self, node: 'Node') -> None:
        self.right = node
    
    def insert_left(self, node: 'Node') -> None:
        self.left = node


if __name__ == "__main__":
    anode = Node(312)
    print(anode)
    bnode = Node(22)
    cnode = Node(44)
    anode.insert_left(bnode)
    anode.insert_right(cnode)
    print(anode.right)
    print(anode.left)

