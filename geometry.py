import math

def rect_area(a: float, b: float) -> float | None:
    if a < 0 or b < 0:
        return None
    return a * b

def rect_perimeter(a: float, b: float) -> float | None:
    if a < 0 or b < 0:
        return None
    return 2 * (a + b)

def rect_diagonal(a: float, b: float) -> float | None:
    if a < 0 or b < 0:
        return None
    return math.hypot(a, b)

def rect_scale(a: float, b: float, k: float):
    if a < 0 or b < 0 or k < 0:
        return None
    return a * k, b * k

def circle_area(r: float) -> float | None:
    if r < 0:
        return None
    return math.pi * r * r

def circle_circumference(r: float) -> float | None:
    if r < 0:
        return None
    return 2 * math.pi * r

def circle_diameter(r: float) -> float | None:
    if r < 0:
        return None
    return 2 * r

def circle_is_unit(r: float) -> bool:
    if r < 0:
        return False
    return abs(r - 1.0) < 1e-9

def circle_scale(r: float, k: float):
    if r < 0 or k < 0:
        return None
    return r * k