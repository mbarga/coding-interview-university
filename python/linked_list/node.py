from typing import Any

class Node:
    value: str
    next: Any

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return(self.value)