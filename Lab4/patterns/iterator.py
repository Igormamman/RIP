import operator

#итератор для работы со списками студентов
class Student_Iterator:
    """Итератор, для работы со списком студентов."""

    def __init__(self, data,key=1):
        self.key=key
        self.data =[]
        self.index = 0
        if key==1:
            for x in data:
                self.data.append(x)
                self.data=sorted(self.data,key=lambda x: x.get_marks(),reverse=False)
        elif key==0:
            for x in data:
                self.data.append(x)
                self.data = sorted(self.data, key=lambda x: x.name, reverse=False)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[self.index-1]