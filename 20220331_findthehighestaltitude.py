def largestAltitude(gain):
    return max(max([sum(gain[:x]) for x in range(len(gain))]), sum(gain))


if __name__ == '__main__':
    print(largestAltitude([-5, 1, 5, 0, -7]))
