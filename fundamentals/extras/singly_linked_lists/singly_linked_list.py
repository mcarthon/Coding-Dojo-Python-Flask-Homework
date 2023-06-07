from node import Node

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self 

    def traverse_and_print(self):
        if self.head == None:
            return self
        
        runner = self.head
        print(runner.value)

        while runner.next != None:
            print(runner.next.value)
            runner = runner.next

        return self

    def traverse(self):
        if self.head == None:
            return self
        
        runner = self.head

        while runner.next != None:
            runner = runner.next

        return self

    def traverse_and_append(self, value):
        if self.head == None:
            return self
        
        runner = self.head
        new_node = Node(value)

        while runner.next != None:
            runner = runner.next

        runner.next = new_node
        new_node.next = None

        return self

    def remove_from_front(self):
        if self.head == None:
            return self

        original_head = self.head
        self.head = original_head.next
        original_head.next = None

        return self

    def remove_from_back(self):
        if self.head == None:
            return self

        if self.head.next == None:
            self.head = None
            return self

        runner = self.head

        while runner.next != None:
            previous_node = runner
            runner = runner.next

        previous_node.next = None

        return self

    def remove_val(self, value):
        if self.head == None:
            return self

        # check if we want to remove the very first value
        runner = self.head
        if runner.value == value:
            self.remove_from_front()
            return self

        # check if we want to remove an intermediate value
        while runner.next != None:
            if runner.next.value == value:
                special_node = runner.next
                runner.next = special_node.next
                special_node = None
                return self
            else:
                runner = runner.next

        # if none of the above, check the last item
        if runner.value == value:
            self.remove_from_back()
        return self

        

    def insert_at(self, value, special_index):
        special_index = int(special_index)

        if (special_index < 0) or (self.head == None and special_index != 0):
            return self
        
        if self.head == None:
            self.add_to_front(value)
            return self
        
        runner = self.head

        # check if we need to change the first value
        if special_index == 0:
            runner.value = value
            return self

        # check if we need to change an intermediate value
        current_index = 1
        while runner.next != None:
            if current_index == special_index:
                runner.next.value = value
                return self
            else:
                runner = runner.next
                current_index += 1
            
        # if none of the above, change the last value
        runner.value = value
        return self

if __name__ == "__main__":
    
    sllist = SinglyLinkedList()

    sllist.add_to_front(3).add_to_front(4).add_to_front(5).add_to_front(6)\
        .traverse_and_append(2).remove_from_front().remove_from_back().remove_val(3)\
            .add_to_front(100).traverse_and_append(101).insert_at(99, 3).traverse_and_print()
    print()

    sllist_edge = SinglyLinkedList()

    sllist_edge.add_to_front(2).remove_from_back().traverse_and_print()