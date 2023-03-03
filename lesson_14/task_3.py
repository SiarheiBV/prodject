class IncorrectUserInputError(Exception):
    ...


class Element:
    def __init__(self, data: int):
        if not 0 <= data <= 10000:
            raise IncorrectUserInputError(f"Number must be in range 0-10000, you input {data}")
        self.data = data
        self.next = None

    def __str__(self):
        # return f"[{self.data}]" # для построчного вывода по одному элементу через цикл for
        return f"[{self.data}] -> {self.next}"    # для красивого вывода всех элементов через метод println без
        # использования цикла и доп переменной для сохранения данных

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data < other.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, element):
        new_element = Element(element)
        current = self.head
        if not self.head:
            self.head = new_element
            self.length += 1
            return
        while current.next:
            current = current.next
        current.next = new_element
        self.length += 1

    def reverse(self):
        current = self.head
        previous = None
        while current:
            temporary = current.next
            current.next = previous
            previous = current
            current = temporary
        self.head = previous

    # 1 вариант. вывода списка через этот метод: [1] -> [2] -> [3] -> [4] -> None

    def println(self):
        return self.head

    # 2 вариант. цикл + доп. переменная для сохранения данных.
    # def println(self):
    #     current = self.head
    #     lst = str(self.head) + "->"
    #     while current.next:
    #         lst += str(current.next) + "->"
    #         current = current.next
    #     return lst

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        return None


link = LinkedList()
link.append(1)
link.append(2)
link.append(3)
link.append(4)

print(link.println())
link.reverse()
print(link.println())
print(link.__len__())
for i in link:
    print(i)
print()
