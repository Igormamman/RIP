from lab_python_oop.Color import Color
from lab_python_oop.Figure import Figure


class Rectangle(Figure):
    type = "Прямоугольник"

    @classmethod
    def get_type(cls):
        return cls.type

    def __init__(self, width_par, height_par, color_par):
        self.width = width_par
        self.height = height_par
        self.colorType = Color()
        self.colorType.color = color_par

    def size(self):
        return self.height * self.width

    def __repr__(self):
        return "Фигура:{} \n Цвет:{} \n Площадь:{} \n Длина:{} \n Ширина:{}"\
            .format(self.type,
                    self.colorType.color,
                    self.size(),
                    self.width,
                    self.height
                    )
