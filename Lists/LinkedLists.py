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

    def insert_last(self, v):
        if self.head is None:
            self.head = LinkedList.Elem(v, None)
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = LinkedList.Elem(v, None)

    def del_first(self):
        if self.head is not None:
            self.head = self.head.next

    def del_max(self):
        if self.head is None:
            return
        pMax = self.head
        ppMax = None
        p = self.head.next
        pp = self.head
        while p is not None:
            if p.val > pMax.val:
                pMax = p
                ppMax = pp
            pp = p
            p = p.next
        if ppMax is not None:
            ppMax.next = pMax.next
        else:
            self.head = pMax.next

    def insert(self, v):
        pNew = LinkedList.Elem(v,None)
        if self.head is None:
            self.head = pNew
            return

        if self.head.val >= v:
            pNew.next = self.head
            self.head = pNew
            return

        p = self.head
        while p.next is not None:
            if p.next.val >= v:
                pNew.next = p.next
                p.next = pNew
                return
            p = p.next
        p.next = pNew

    def search1(self, v):
        p = self.head
        while p is not None and p.val != v:
            p = p.next
        return p

    def print_rev_rec(self):
        def _print_rev(tmp):
            if tmp is None:
                return
            _print_rev(tmp.next)
            print(tmp.val)

        _print_rev(self.head)


if __name__ == "__main__":
    l = LinkedList()
    l.insert_front(5)
    l.insert_front(4)
    l.insert_front(6)
    l.insert_last(6)
    l.del_first()
    l.del_max()
    # l.print_all()
    l.insert(6)
    l.insert(8)
    l.insert(7)
    # l.print_all()
    l.print_rev_rec()


