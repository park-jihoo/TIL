def complex_number_multiply(num1: str, num2: str) -> str:
    r1, i1 = num1.split('+')
    r2, i2 = num2.split('+')
    r1, r2, i1, i2 = int(r1), int(r2), int(i1[:-1]), int(i2[:-1])
    return str(r1*r2 - i1*i2) + "+" + str(r1*i2 + r2*i1) +"i"

if __name__ == '__main__':
    print(complex_number_multiply("1+1i", "1+1i"))