PI = 3.14


def circle_area(r: float) -> float:
    """Функция расчета площади окружности"""

    circle_area = PI * r**2

    return circle_area


def format_description(r: float, area: float):
    """Форматированный вывод информации о площади окружности"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: float) -> None:
    """Получение информации об окружности"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_circle_info(radius)
