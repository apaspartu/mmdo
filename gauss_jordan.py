def gauss_jordan(A: list[list[float]], b: list[float]) -> list[float]:
    n = len(A)
    C = [[A[i][j] for j in range(n)] for i in range(n)]
    x = b[:]

    for i in range(n):
        d = C[i][i]
        if d == 0:
            d = d + 0.000001

        for j in range(n):
            C[i][j] = C[i][j] / d
        x[i] = x[i] / d

        for m in range(n):
            if m != i:
                p = C[m][i]
                for j in range(n):
                    C[m][j] = C[m][j] - p * C[i][j]
                x[m] = x[m] - p * x[i]
    return x


if __name__ == '__main__':
    TITLE = "<< Програма для розв'язування систем лінійних рівнянь методом Гауса-Жордана >>"
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    FREE_VAR_PROMPT = 'Введіть елементи стовпця вільних змінних, розділені пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів: {} < {}'
    ZERO_DIVISION = "Дана система рівнянь не сумісна і не має розв'язків."
    OUTPUT_PROMPT = "Розв'язок системи:"

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

        print(FREE_VAR_PROMPT)
        b = list(map(float, input().split()))

        if len(b) != len(A):
            print(ERROR_PROMPT.format(len(b), len(A)))
            quit()

        try:
            X = gauss_jordan(A, b)
        except ZeroDivisionError:
            print(ZERO_DIVISION)
        else:
            solution = [f'x{i + 1} = {x:zg}' for i, x in enumerate(X)]
            print(OUTPUT_PROMPT, *solution, sep='\n')
