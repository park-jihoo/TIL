def angle_clock(hour: int, minutes: int) -> float:
    hour = hour % 12
    angle = 30 * hour - 5.5 * minutes
    if abs(angle) > 180:
        return 360 - abs(angle)
    return abs(angle)


if __name__ == '__main__':
    print(angle_clock(1, 57))
