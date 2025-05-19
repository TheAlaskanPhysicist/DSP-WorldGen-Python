import math












def rand_normal(mean: float, std: float, r1: float, r2: float) -> float:
    return mean + std * math.sqrt(-2.0 * math.log(1.0 - r1)) * math.sin(2.0 * math.pi * r2)

def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min(value, max_value), min_value)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t