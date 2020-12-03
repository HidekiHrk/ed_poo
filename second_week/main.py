class Node:
    def __init__(self, value, next_value: 'Node' = None):
        self.value = value
        self.next = next_value


class ChainedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def push_to_start(self, value):
        node = Node(value, self.head)
        if not self.head:
            self.head = self.tail = node
        else:
            self.head = node

    def push(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def remove_from_start(self):
        if self.head is None:
            print('The list is empty')
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def pop(self):
        if self.tail is None:
            print('The list is empty')
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            self.tail = current
            current.next = None

    def navigate(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    @property
    def length(self) -> int:
        size = 0
        for _ in self.navigate():
            size += 1
        return size

    def print_list(self):
        print('[', end='')
        for node in self.navigate():
            print(node.value, end=', ' if node != self.tail else ']\n')

    def search(self, value) -> bool:
        for node in self.navigate():
            if node.value == value:
                return True
        return False

    def update(self, item, value):
        for node in self.navigate():
            if node.value == item:
                node.value = value

    def insert(self, value, pos: int):
        if pos < 0:
            print('Invalid position')
            return

        if pos == 0:
            self.push_to_start(value)
        elif pos >= self.length:
            self.push(value)
        else:
            new_node = Node(value)
            current_pos = 0
            for node in self.navigate():
                if current_pos == pos - 1:
                    new_node.next = node.next
                    node.next = new_node
                    break
                current_pos += 1

    def remove(self, value):
        if self.head is None:
            print('Empty list')
            return

        if self.head.value == value:
            self.remove_from_start()
        elif self.tail.value == value:
            self.pop()
        else:
            for node in self.navigate():
                if node.next and node.next.value == value:
                    node.next = node.next.next
                    break

    def concat(self, other: 'ChainedList'):
        self.tail.next = other.head
        self.tail = other.tail


class NumList(ChainedList):
    def separate_in_pair_odd(self) -> ('NumList', 'NumList',):
        pair = NumList()
        odd = NumList()
        for node in self.navigate():
            if node.value % 2 == 0:
                pair.push(node.value)
            else:
                odd.push(node.value)
        return pair, odd,


num_list = NumList()
for num in range(20):
    num_list.push(num)

num_list.print_list()
list_1, list_2 = num_list.separate_in_pair_odd()
list_1.print_list()
list_2.print_list()
