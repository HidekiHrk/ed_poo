class Stack:
    def __init__(self):
        self.__items = []

    @property
    def size(self):
        return len(self.__items)

    def push(self, value):
        self.__items.insert(0, value)

    def pop(self):
        return self.__items.pop(0)

    def top(self):
        return self.__items[0]

    def iter_all(self):
        while True:
            try:
                yield self.pop()
            except IndexError:
                break

    def insert_at_bottom(self, item):
        if self.size == 0:
            self.push(item)
        else:
            aux = self.top()
            self.pop()
            self.insert_at_bottom(item)
            self.push(aux)

    def view(self):
        print(self.__items)


def is_palindrome(arr: list):
    char_stack = Stack()
    reversed_char_stack = Stack()
    for char in arr:
        char_stack.push(char)
        reversed_char_stack.insert_at_bottom(char)

    for _ in range(char_stack.size):
        item1 = char_stack.pop()
        item2 = reversed_char_stack.pop()
        if item1 != item2:
            return False
    return True


def main():
    word = list(input("Check palindrome: "))
    print(is_palindrome(word))


main()
