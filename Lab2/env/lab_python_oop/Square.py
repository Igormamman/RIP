from lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):
    type = "Квадрат"

    def __init__(self, width_par, color_par):
        super().__init__(width_par, width_par, color_par)

    def __repr__(self):
        return "Фигура:{} \n Цвет:{} \n Площадь:{} \n Сторона {}"\
            .format(self.type,
                    self.colorType.color,
                    self.size(),
                    self.width,
                    )