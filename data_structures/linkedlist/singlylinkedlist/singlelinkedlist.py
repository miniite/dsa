class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    # Insert at specific position (0-based index)
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node


    # Delete at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next


    # Delete at the end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


    # Delete at specific position (0-based index)
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None or current.next is None:
            print("Position out of range")
            return
        current.next = current.next.next


    # Delete first occurrence of a value
    def delete_first_occurrence(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.delete_at_beginning()
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            print("Value not found")
            return
        current.next = current.next.next


    # Search for an element by value
    def search_by_value(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1


    # Search by index (0-based index)
    def search_by_index(self, index):
        if index < 0:
            print("Invalid index")
            return None
        current = self.head
        for i in range(index):
            if current is None:
                print("Index out of range")
                return None
            current = current.next
        if current is None:
            print("Index out of range")
            return None
        return current.data


    # Update value at beginning
    def update_at_beginning(self, new_value):
        if self.head is None:
            print("List is empty")
            return
        self.head.data = new_value


    # Update value at end
    def update_at_end(self, new_value):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        current.data = new_value


    # Update value at specific position (0-based index)
    def update_at_position(self, new_value, position):
        if position < 0:
            print("Invalid position")
            return
        current = self.head
        for i in range(position):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        current.data = new_value


    # Traverse and print the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    # Get length of the list
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    

    def find_middle_two_pointers(self):
        if self.head is None:
            print("List is empty")
            return None
        if self.head.next is None:
            return self.head.data
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next.data
    

    def find_middle_by_length(self):
        if self.head is None:
            print("List is empty")
            return None
        length = self.get_length()
        middle_index = length // 2
        current = self.head
        for i in range(middle_index):
            current = current.next
        return current.data
    

    @staticmethod
    def merge_sorted_lists_iterative(list1, list2):
        result = LinkedList()
        dummy = Node(0)
        current = dummy
        
        p1 = list1.head
        p2 = list2.head
        
        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        current.next = p1 if p1 else p2
        
        result.head = dummy.next
        return result
        

