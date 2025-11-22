from enum import Enum


# Enums
class EcologistCellType(Enum):
    SOIL = "Почва"
    PLANT = "Растение"
    SAMPLE = "Проба"
    PROCESSED = "Обработано"
    POLLUTION = "Загрязнение"
    FINISH = "Финиш"
    CONTROL = "Контроль"


class EcologistDirectionType(Enum):
    FORWARD = "ЭкологВперед"
    BACKWARD = "ЭкологНазад"
    LEFT = "ЭкологВлево"
    RIGHT = "ЭкологВправо"
    DIAG_UP = "ДиагЭкологВ"
    DIAG_DOWN = "ДиагЭкологН"


class BasicDirectionType(Enum):
    NORTH = "С"
    SOUTH = "Ю"
    WEST = "З"
    EAST = "В"
    NORTH_WEST = "СЗ"
    SOUTH_EAST = "ЮВ"


# Основные классы
class RobotEcologistCell:
    def __init__(self, has_robot: bool, cell_type: EcologistCellType):
        self.has_robot = has_robot
        self.cell_type = cell_type

    def __str__(self):
        return f"[{self.cell_type.value}]"


class RobotEcologistMaze:
    # ЛабиринтРоботЭколог
    def __init__(self, width: int, height: int, cells: list):
        """
        :param width: ширина
        :param height: длина
        :param cells: ячейки
        """
        self.width = width
        self.height = height
        self.cells = cells

    def initialize_maze(self, cell_type: EcologistCellType):
        # Создаем двумерный массив
        self.cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                new_cell = RobotEcologistCell(False, cell_type)
                row.append(new_cell)
            self.cells.append(row)
        print(f"Лабиринт {self.width}x{self.height} инициализирован типом {cell_type.value}")


if __name__ == '__main__':
    print("Запуск main.py")
