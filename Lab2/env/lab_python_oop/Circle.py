from lab_python_oop.Color import Color
from lab_python_oop.Figure import Figure
from math import pi


class Circle(Figure):

    type="Круг"

    @classmethod
    def get_type(cls):
        return cls.type

    def __init__(self,radius,color_par):
        self.r = radius
        self.colorType = Color()
        self.colorType.color = color_par

    def size(self):
        return 2*pi*self.r*self.r

    def __repr__(self):
        return "Фигура:{} \n Цвет:{} \n Площадь:{} \n Радиус" \
            .format(self.type,
                    self.colorType.color,
                    round(self.size(), 2),
                    self.r
                    )