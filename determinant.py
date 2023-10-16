def determinant(A: list[list[float]]) -> float:
    n = len(A)
    B = [[A[i][j] for j in range(n)] for i in range(n)]
    d = 1
    for i in range(n):
        k = B[i][i]
        if k == 0:
            return 0
        d *= k
        for j in range(n):
            B[i][j] = B[i][j] / k
        for m in range(n):
            if m != i:
                r = B[m][i]
                for j in range(n):
                    B[m][j] = B[m][j] - r * B[i][j]
    p = 1
    for i in range(n):
        p *= B[i][i]
    return p * d


if __name__ == '__main__':
    TITLE = '<< Програма для знаходження визначника матриці >>'
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів рядка: {} < {}'
    OUTPUT_PROMPT = 'Визначник: D = {:zg}'

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

        det = determinant(A)
        print(OUTPUT_PROMPT.format(det))
