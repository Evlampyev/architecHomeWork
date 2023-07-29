from figure import Figure


class Square(Figure):

    def __init__(self, width):
        self.__width = width  # private

    def get_area(self):
        return self.__width * self.__width
