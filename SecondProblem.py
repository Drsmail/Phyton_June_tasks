# ---------------------------------------
# SECOND PROBLEM
# ---------------------------------------
from abc import ABC, abstractmethod


class FIFOInterface(ABC):
    """Интерфейс для циклического буфера FIFO."""

    def __init__(self, capacity=1):
        self.capacity = max(capacity, 1)  # Емкость буфера (минимум 1)
        self.write_index = 0  # Индекс чтения (начало)
        self.read_index = 0    # Индекс записи (конец)
        self.size = 0   # Текущий размер буфера

    @abstractmethod
    def put(self, el):
        """Добавить элемент в очередь."""
        pass

    @abstractmethod
    def get(self):
        """Получить первый элемент из очереди."""
        pass

    @abstractmethod
    def size(self):
        """Получить текущий размер очереди."""
        pass

# Быстрое и не безопасное решение, которе будет перезаписывать данные поверх друг-друга,
# если не уследить за переполнением
class ArrayFIFO(FIFOInterface):
    """Реализация небезопасного и быстрого FIFO"""

    def __init__(self, capacity=1):
        super().__init__(capacity)
        self.__Buffer = [0] * self.capacity # Let's pretend it's a static Array

    def put(self, el):
        self.__Buffer[self.write_index % self.capacity] = el
        self.write_index += 1
        self.size += 1


    def get(self):
        el = self.__Buffer[self.read_index % self.capacity]
        self.read_index += 1
        self.size -= 1
        return el

    def size(self):
        # Will work incorrectly after data override
        return self.size

class LinkedFIFO(FIFOInterface):
    """Реализация FIFO с использованием связного списка."""

    class Node:
        def __init__(self, el=None, next=None):
            self.val = el
            self.next = next

    def __init__(self, capacity):
        # Capacity is inf in this class
        super().__init__(capacity)
        self.write_index = None
        self.read_index = None

    def get(self):
        if self.size == 0:
            raise ValueError("Очередь пуста")
        r_val = self.read_index.val
        # Unlinking Node for GC to collect
        self.read_index = self.read_index.next
        self.size -= 1
        return r_val

    def put(self, el):
        new_node = self.Node(el)

        if self.size == 0:
            self.write_index = new_node
            self.read_index = new_node
        else:
            self.write_index.next = new_node
            self.write_index = new_node
        self.size += 1

    def size(self):
        return self.size


if __name__ == '__main__':
    print("Testing unsafe ArrayFIFO:")
    test_size = 5
    fifo = ArrayFIFO(test_size)
    print("Array FIFO input:")
    for i in range(test_size + 3):  # Example of unsafe override
        fifo.put(i)
        print(f" {i},", end="")

    print("\nArray FIFO output:")
    for i in range(test_size):
        print(f" {fifo.get()},", end="")

    print("\nTesting LinkedFIFO:")
    test_size = 5
    test_override = 3
    fifo = LinkedFIFO(test_size)
    print("Array FIFO input:")
    for i in range(test_size + test_override):  # we can handel this
        fifo.put(i)
        print(f" {i},", end="")

    print("\nArray FIFO output:")
    for i in range(test_size + test_override):
        print(f" {fifo.get()},", end="")

