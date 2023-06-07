from singly_linked_list import SinglyLinkedList

class DoublyLinkedList(SinglyLinkedList):

    def __init__(self):
        self.head = None

    def insert_between(self, value, special_index):
        special_index = special_index - 1

        self.insert_at(value = value, special_index = special_index)    
        return self
