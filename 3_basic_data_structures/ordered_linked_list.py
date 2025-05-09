class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)
    

class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        unordered_list = []
        while current is not None:
            unordered_list.append(current._data)
            current = current._next
        return unordered_list

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count
    
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
    
    def append(self, item):
        current = self.head
        while current._next is not None:
            current = current._next
        current._next = Node(item)

    def insert(self, item, insert_index):
        current = self.head
        previous = None
        current_index = 0
        while current is not None:
            if current_index == insert_index:
                # insert here
                inserted_node = Node(item)
                inserted_node._next = current._next
                if previous is None:
                    self.head = inserted_node
                else:
                    previous._next = inserted_node
                break
            else:
                previous = current
                current = current._next
                current_index += 1
        
    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            index += 1
            current = current.next
        return 'Not found'

        


my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
print(my_list.__str__())
my_list.append(34)
print(my_list.__str__())
my_list.insert('asdf', 1)
print(my_list.__str__())
print(my_list.index('asdf'))