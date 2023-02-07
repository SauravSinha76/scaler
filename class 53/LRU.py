class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prv = None

class LRU:


    def __init__(self,capacity):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prv = self.head
        self.hm ={}
        self.length = 0


    def remove(self,node):
        self.length -= 1
        node.prv.next = node.next
        node.next.prv = node.prv


    def add_at_tail(self, node):
        node.next = self.tail
        node.prv = self.tail.prv
        self.tail.prv.next = node
        self.tail.prv = node
        self.hm[node.key] = node
        self.length += 1


    def get(self,key):
        if key not in self.hm:
            return -1

        else:
            node = self.hm[key]
            self.remove(node)
            self.add_at_tail(node)
            return node.value


    def set(self,key,value):
        if key not in self.hm:
            node = Node(key, value)
            if self.length < self.capacity:
                self.add_at_tail(node)
            else:
                self.hm.pop(self.head.next.key)
                self.remove(self.head.next)
                self.add_at_tail(node)

        else:
            node = self.hm[key]
            node.value = value
            self.remove(node)
            self.add_at_tail(node)


    def printlru(self):
        temp = self.head
        while temp:
            print(f"[{temp.key},{temp.value}]",end=" ")
            temp = temp.next

# lru = LRU(2)
# lru.set(1,10)
# lru.set(5,25)
#
# lru.printlru()
# print(lru.get(5))
# print(lru.get(1))
# lru.printlru()
# print(lru.get(10))
# lru.set(6,14)
# lru.printlru()
# print(lru.get(5))

lru = LRU(1)

lru.set(2,1)
lru.set(2,2)

# lru.printlru()

print(lru.get(2))

lru.set(1,1)
lru.set(4,1)
lru.printlru()
print(lru.get(2))

# lru = LRU(2)
#
# print(lru.get(2))
#
# lru.set(2,6)
#
# print(lru.get(1))
#
# lru.set(1,5)
# lru.set(1,2)
# lru.printlru()
# print(lru.get(1))
# print(lru.get(2))


