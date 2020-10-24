import gen_random


class Unique:
    """Итератор, оставляющий только уникальные значения."""
    def __init__(self, data):
        self.used_elements = set()
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current)
                    return current





