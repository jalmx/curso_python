import math


class Area:

    @staticmethod
    def get_circle(radio=1):
        return math.pi * pow(radio, 2)

    @staticmethod
    def get_square(side=1):
        return pow(side, 2)

    @staticmethod
    def get_rectangle(base, high):
        return base * high
