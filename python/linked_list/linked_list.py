from node import Node

class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    def append(self, value):
        nn = Node(value)
        if self.head is None:
            self.head = nn
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = nn

    def value_at(self):
        pass

    def pop_front(self):
        pop = self.head
        self.head = self.head.next
        return pop.value

    def pop_back(self):
        cur = self.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        if prev:
            prev.next = None
        return cur.value

    def value_at(self, index):
        pass

    def push_front(self, value):
        nn = Node(value)
        nn.next = self.head
        self.head = nn

    def push_back(self, value):
        nn = Node(value)
        cur = self.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        if prev:
            prev.next = nn

    def front(self):
        return self.head.value
         
    def back(self):
        cur = self.head
        while cur:
            prev = cur
            cur = cur.next
        return prev.value

    def __iter__(self):
        self.next = self.head
        return self

    def __next__(self):
        if self.next:
            prev = self.next
            self.next = self.next.next
            return prev
        else:
            raise StopIteration

    def __len__(self):
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def __str__(self):
        output = ""
        cur = self.head
        while cur.next is not None:
            output += f"{cur.value}->"
            cur = cur.next
        output += cur.value
        return output


if __name__ == "__main__":
    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.push_back('z')
    ll.push_front('1')
    print(ll)
    print(ll.front())
    print(ll.back())
    print(len(ll))
    for l in ll:
        print(l)