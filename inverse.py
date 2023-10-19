def inverse(A: list[list[float]]) -> list[list[float]]:
    n = len(A)
    B = [[A[i][j] for j in range(n)] for i in range(n)]
    I = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        d = B[i][i]
        if d == 0:
            d = d + 0.000001

        for j in range(n):
            B[i][j] = B[i][j] / d
        for j in range(n):
            I[i][j] = I[i][j] / d

        for m in range(n):
            if m != i:
                p = B[m][i]
                for j in range(n):
                    B[m][j] = B[m][j] - p * B[i][j]
                for j in range(n):
                    I[m][j] = I[m][j] - p * I[i][j]
    return I


if __name__ == '__main__':
    TITLE = "<< Програма для знаходження оберненої матриці >>"
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів рядка: {} < {}'
    ZERO_DETERMINANT = 'Дана матриця не має оберненої, тому що її визначник дорівнює нулю.'
    OUTPUT_PROMPT = 'Обернена матриця:'

    print(TITLE + '\n')

    print(SIZE_PROMPT)
    n = int(input())

    if n > 0:
        print(ELEMENTS_PROMPT)
        A = []
        for _ in range(n):
            row = list(map(float, input().split()))
            if len(row) < n:
                print(ERROR_PROMPT.format(len(row), n))
                quit()
            A.append(row)

        try:
            R = inverse(A)
        except ZeroDivisionError:
            print(ZERO_DETERMINANT)
        else:
            print(OUTPUT_PROMPT)
            for row in R:
                print(*(f'{i:.3f}' for i in row))
