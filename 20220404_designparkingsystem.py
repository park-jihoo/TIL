class ParkingSystem:
    slot = [0, 0, 0]

    def __init__(self, big: int, medium: int, small: int):
        self.slot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slot[carType - 1] == 0:
            return False
        else:
            self.slot[carType - 1] -= 1
            return True


if __name__ == '__main__':
    ps = ParkingSystem(1, 1, 0)
    print(ps.addCar(1))
    print(ps.addCar(2))
    print(ps.addCar(3))
    print(ps.addCar(1))
    print(ps.slot)
