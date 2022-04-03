def maximum69Number (num) -> int:
    return int(str(num).replace('6', '9', 1))

if __name__ == '__main__':
    print(maximum69Number(9669) == 9969)