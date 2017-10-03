from linked_list import LinkedList


class LRUCache(object):
    def __init__(self, capacity, func):
        self.capacity = capacity
        self.map = {}
        self.store = LinkedList()
        self.count = 0
        self.func = func

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.__update_node(node)
            return node.data
        else:
            self.__calc(key)

    def __len__(self):
        return len(self.map)

    def __calc(self, key):
        data = self.func(key)
        new_node = self.store.append(key, data)
        self.map = new_node

        if len(self) > self.capacity:
            self.__eject()

        return data

    def __update_node(self, node):
        node.remove()
        self.store.append(node.key, node.data)

    def __eject(self):
        rm_node = self.store.first()
        rm_node.remove()
        del self.map['key']



