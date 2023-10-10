def transpose(A: list[list[float]], m: int, n: int) -> list[list[float]]:
    T = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]
    return T


def gauss_jordan(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m_a = len(A)
    n_b = len(B[0])
    for i in range(m_a):
        d = A[i][i]
        for j in range(m_a):
            A[i][j] = A[i][j] / d

        for j in range(n_b):
            B[i][j] = B[i][j] / d

        for m in range(m_a):
            if m != i:
                p = A[m][i]
                for j in range(m_a):
                    A[m][j] = A[m][j] - p * A[i][j]

                for j in range(n_b):
                    B[m][j] = B[m][j] - p * B[i][j]
    return B


if __name__ == '__main__':
    TITLE = "<< Програма для розв'язування систем лінійних рівнянь методом Гауса-Жордана >>"
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    FREE_VAR_PROMPT = 'Введіть елементи стовпця вільних змінних, розділені пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів: {} < {}'
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
        free_vars = list(map(float, input().split()))

        b = transpose([free_vars], 1, len(free_vars))
        if len(b) != len(A):
            print(ERROR_PROMPT.format(len(b), len(A)))
            quit()

        X = gauss_jordan(A, b)

        solution = [f'x{i + 1} = {x}' for i, x in enumerate(*transpose(X, len(X), 1))]

        print(OUTPUT_PROMPT, *solution, sep='\n')
