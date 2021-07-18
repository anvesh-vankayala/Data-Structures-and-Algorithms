class Node:
    def __init__(self,prev=None, next = None, data= None) -> None:
        self.prev = prev
        self.next = next
        self.data = data

class Deque:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def push_front(self, key):
        if self.empty():
            self.head.data = key
        else:
            holder = self.head
            self.head = Node(next = holder, data = key)
            holder.prev = self.head
            #self.tail = holder
        self.length += 1
        return 'ok'

    def push_back(self, key):
        if self.empty():
            self.head.data = key
        else:
            new_node = Node(prev= self.tail,data=key)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return 'ok'

    def pop_front(self):
        if self.head.data == None:
            return 'error'
        temp_node = self.head
        if temp_node.next == None:
            self.head = Node()
            self.tail = self.head
        else:
            temp_node.prev = None
            self.head = temp_node.next
            self.head.prev = None
        self.length -= 1
        return temp_node.data

    def pop_back(self):
        if self.tail.data == None:
            return 'error'
        temp_node = self.tail
        if self.tail.prev == None:
            self.head = Node()
            self.tail = self.head
        else:
            temp_node = self.tail
            self.tail = temp_node.prev
            self.tail.next = None
        self.length -= 1
        return temp_node.data    

    def front(self):
        if self.head.data == None:
            return 'error'
        else:
            return self.head.data
        

    def back(self):
        if self.tail.data == None:
            return 'error'
        else:
            return self.tail.data

    def clear(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0
        return 'ok'

    def size(self):
        return self.length

    def empty(self):
        return self.head.data == None



def process_deque(commands):
    op = []
    dq = Deque()
    for i in commands:
        if ' ' in i:
            mthd,param = i.split()
            mthd = 'dq.'+mthd
            op.append(eval(mthd)(int(param)))
        else:
            mthd = 'dq.'+i
            op.append(eval(mthd)())
    return op

#process_deque(["push_front 1","push_front 2","push_back 6","front","back","clear","size","back"])
#process_deque(["pop_front", "back", "push_back 2", "size"])
#process_deque(["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"])

# dq = Deque()
# print(dq.push_front(1))
# print(dq.push_front(2))
# print(dq.push_back(6))
# print(dq.pop_front())
# print(dq.pop_back())
# print(dq.clear())
# print(dq.size())
# print(dq.back())
# #print(dq)
