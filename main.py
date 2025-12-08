from enum import Enum

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


class RobotEcologistCell:
    def __init__(self, has_robot: bool, cell_type: EcologistCellType):
        self.has_robot = has_robot
        self.cell_type = cell_type

    def __str__(self):
        return f"[{self.cell_type.value}]"


class RobotEcologistMaze:
    def __init__(self, width: int, height: int, cells: list):
        self.width = width
        self.height = height
        self.cells = cells

    def initialize_maze(self, cell_type: EcologistCellType):
        self.cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                new_cell = RobotEcologistCell(False, cell_type)
                row.append(new_cell)
            self.cells.append(row)
        print(f"Лабиринт {self.width}x{self.height} инициализирован типом {cell_type.value}")

    def get_neighbor_cell(self, current_cell: RobotEcologistCell, direction: EcologistDirectionType):
        current_x, current_y = -1, -1
        found = False
        
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x] is current_cell:
                    current_x = x
                    current_y = y
                    found = True
                    break
            if found:
                break
        
        if not found:
            return None

        dx, dy = 0, 0
        
        if direction == EcologistDirectionType.FORWARD:
            dy = 1
        elif direction == EcologistDirectionType.BACKWARD:
            dy = -1
        elif direction == EcologistDirectionType.RIGHT:
            dx = 1
        elif direction == EcologistDirectionType.LEFT:
            dx = -1
        elif direction == EcologistDirectionType.DIAG_UP:
            dx = -1
            dy = 1
        elif direction == EcologistDirectionType.DIAG_DOWN:
            dx = 1
            dy = -1

        new_x = current_x + dx
        new_y = current_y + dy

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            return self.cells[new_y][new_x]
        else:
            return None
        
    def get_iterator(self, robot):
        return SnakeIterator(robot)


class RobotEcologist:
    def __init__(self, maze: RobotEcologistMaze):
        self.maze = maze
        self.current_cell = None  

    def set_start_position(self, x: int, y: int):
        if 0 <= y < self.maze.height and 0 <= x < self.maze.width:
            target = self.maze.cells[y][x]
            if target.cell_type in [EcologistCellType.POLLUTION, EcologistCellType.CONTROL]:
                print("Ошибка: Нельзя стартовать с запрещенной ячейки")
                return
            
            self.current_cell = target
            self.current_cell.has_robot = True
            print(f"Робот установлен в позицию {x}, {y}")
        else:
            print("Ошибка: Координаты вне лабиринта")

    def _move(self, direction: EcologistDirectionType):
        if not self.current_cell:
            return None
        
        neighbor = self.maze.get_neighbor_cell(self.current_cell, direction)

        if neighbor:
            if neighbor.cell_type in [EcologistCellType.POLLUTION, EcologistCellType.CONTROL]:
                return None
            
            self.current_cell.has_robot = False  
            self.current_cell = neighbor
            self.current_cell.has_robot = True   
            return self.current_cell
        
        return None
    
    def move_forward(self):
        return self._move(EcologistDirectionType.FORWARD)
    def move_backward(self):
        return self._move(EcologistDirectionType.BACKWARD)
    def move_left(self):
        return self._move(EcologistDirectionType.LEFT)
    def move_right(self):
        return self._move(EcologistDirectionType.RIGHT)
    def move_up_diag(self):
        return self._move(EcologistDirectionType.DIAG_UP)
    def move_down_diag(self):
        return self._move(EcologistDirectionType.DIAG_DOWN)

    def process_plant(self):
        """
        Метод: Растение()
        Действие: Заменяет Растение -> Проба
        """
        if self.current_cell and self.current_cell.cell_type == EcologistCellType.PLANT:
            self.current_cell.cell_type = EcologistCellType.SAMPLE
            print(f"Ячейка обработана: Растение -> Проба")
        else:
            print("Здесь нет растения для обработки")

    def process_sample(self):
        """
        Метод: Проба()
        Действие: Заменяет Проба -> Обработано
        """
        if self.current_cell and self.current_cell.cell_type == EcologistCellType.SAMPLE:
            self.current_cell.cell_type = EcologistCellType.PROCESSED
            print(f"Ячейка обработана: Проба -> Обработано")
        else:
            print("Здесь нет пробы для анализа")




class SnakeIterator:
    def __init__(self, robot: RobotEcologist):
        self.robot = robot
        self.going_right = True  

    def next_step(self):
        """
        Выполняет один шаг алгоритма.
        Возвращает True, если ход был сделан.
        Возвращает False, если обход завершен.
        """
        
        moved = None
        if self.going_right:
            moved = self.robot.move_right()
        else:
            moved = self.robot.move_left()

        if moved:
            return True

        moved_up = self.robot.move_forward() 

        if moved_up:
            self.going_right = not self.going_right
            return True
        
        return False


if __name__ == '__main__':
    print("Запуск main.py")