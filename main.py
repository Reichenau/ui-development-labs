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

if __name__ == '__main__':
    print("Запуск main.py")