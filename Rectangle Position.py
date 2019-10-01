def tri_compare(x, y):
    position_a = x.get_top() - y.get_top()
    position_b = x.get_left() - y.get_left()
    position_c = x.get_right() - y.get_right()
    position_d = x.get_bottom() - y.get_bottom()
    if position_a >= 0 and position_b >= 0 and position_c <= 0 and position_d <= 0:
        print('Inside')
    else:
        print('Not inside')


class Rectangle:
    def __init__(self, left, top, width, height):
        self.__top = self.set_top(top)
        self.__left = self.set_left(left)
        self.__bottom = self.set_bottom(top, height)
        self.__right = self.set_right(left, width)

    def get_top(self):
        return self.__top

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_bottom(self):
        return self.__bottom

    def set_top(self, top):
        if isinstance(top, float):
            return top
        raise Exception

    def set_left(self, left):
        if isinstance(left, float):
            return left
        raise Exception

    def set_right(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a + b
        raise Exception

    def set_bottom(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a + b
        raise Exception


tri_one = list(map(float, input().split()))
tri_two = list(map(float, input().split()))

triangle_a = Rectangle(tri_one[0], tri_one[1], tri_one[2], tri_one[3])
triangle_b = Rectangle(tri_two[0], tri_two[1], tri_two[2], tri_two[3])

tri_compare(triangle_a, triangle_b)