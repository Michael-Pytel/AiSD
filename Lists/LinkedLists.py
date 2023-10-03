class LinkedList:
    class Elem:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self,head=None):
        self.head = head
    def print_all(self):
        p = self.head
        while p is not None:
            print(p.val)
            p = p.next

    def insert_front(self, v):
        p = LinkedList.Elem(v, None)
        p.next = self.head
        p.val = v
        self.head = p

list = LinkedList()
list.insert_front(5)
list.insert_front(4)
list.insert_front(6)
list.print_all()


