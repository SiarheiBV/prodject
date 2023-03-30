class Vector:

    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def length(self) -> int:
        x1, y1 = self.point_1
        x2, y2 = self.point_2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __lt__(self, other) -> bool:
        return self.length() < other.length()

    def __gt__(self, other) -> bool:
        return self.length() > other.length()

    def __le__(self, other) -> bool:
        return self.length() <= other.length()

    def __ge__(self, other) -> bool:
        return self.length() >= other.length()

    def __eq__(self, other) -> bool:
        return self.length() == other.length()

    def __ne__(self, other) -> bool:
        return self.length() != other.length()


vector_1 = Vector((1, 1), (2, 4))
vector_2 = Vector((1, 1), (2, 4))
print(vector_1 < vector_2)
print(vector_1 < vector_2)
print(vector_1 >= vector_2)
print(vector_1 <= vector_2)
print(vector_1 == vector_2)
print(vector_1 != vector_2)
