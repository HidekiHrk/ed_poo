class Queue:
    def __init__(self):
        self.__items = []

    @property
    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pull(self):
        return self.__items.pop(0)

    def iter_all(self):
        while self.size > 0:
            yield self.pull()


class Stack:
    def __init__(self):
        self.__items = []

    @property
    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.insert(0, item)

    def pop(self):
        return self.__items.pop(0)

    def iter_all(self):
        while self.size > 0:
            yield self.pop()

    def stack_reverse(self):
        aux = Stack()
        saux = Stack()
        for item in self.iter_all():
            aux.push(item)
        for item in aux.iter_all():
            saux.push(item)
        for item in saux.iter_all():
            self.push(item)

    def queue_reverse(self):
        aux = Queue()
        for item in self.iter_all():
            aux.push(item)
        for item in aux.iter_all():
            self.push(item)

    def view(self):
        print(self.__items)


def main():
    stack = Stack()
    is_running = True
    operations = {
        'I': lambda: stack.push(input('item: ')),
        'P': lambda: stack.pop(),
        'V': lambda: stack.view(),
        'SR': lambda: stack.stack_reverse(),
        'QR': lambda: stack.queue_reverse()
    }
    while is_running:
        print('I = insert a item into stack;\n'
              'P = pop a item from stack;\n'
              'V = view stack;\n'
              'SR = reverse stack with stacks;\n'
              'QR =  reverse stack with queues;\n'
              'E = exit program')

        operation_str = input('operation: ').upper()
        if operation_str == 'E':
            is_running = False
        else:
            operation = operations.get(operation_str)
            if operation is None:
                print('Invalid operation')
            else:
                operation()

main()