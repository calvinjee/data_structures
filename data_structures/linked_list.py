class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self


class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, val):
        node = Node(key, val)

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return node

    def includes(self, key):
        for node in self:
            if node.key == key:
                return True

        return False

    def first(self):
        return self.head.next if self.head.next != self.tail else None

    def last(self):
        return self.tail.prev if self.tail.prev != self.head else None

    def get(self, key):
        for node in self:
            if node.key == key:
                return node.data

    def update(self, key, data):
        for node in self:
            if node.key == key:
                node.data = data
                return node

    def remove(self, key):
        for node in self:
            if node.key == key:
                node.remove()
                return node

    def __str__(self):
        return ', '.join([str([node.key, node.data]) for node in self])

    def __iter__(self):
        current = self.head.next
        while current.next is not None:
            node = current
            current = current.next
            yield node
        # return self

    # def __next__(self):
    #     current = self.head.next
    #     if current.next is None:
    #         raise StopIteration
    #     else:
    #         return current
    #         current = current.next

    # next = __next__


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1, 1)
    ll.append(2, 4)
    ll.append(3, 9)

    print(ll)
    # print(ll.next().data)
    # print(ll.next().data)
    # print(ll.next().data)
    # print(ll.next().data)

    for node in ll:
        print(node.data)

    print(ll.get(1))

    print(ll.includes(4))

    ll.remove(3)
    print(ll)

    print(ll.update(5, 7))
    print(ll)






