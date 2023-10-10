from determinant import determinant
from gauss_jordan import gauss_jordan


def inverse(A: list[list[float]]) -> list[list[float]]:
    n = len(A)
    I = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    D = determinant(A)
    if D == 0:
        raise ValueError('Дана матриця не має оберненої тому, що її визначник дорівнює нулю')

    return gauss_jordan(A, I)


if __name__ == '__main__':
    TITLE = "<< Програма для знаходження оберненої матриці >>"
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів рядка: {} < {}'
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

        R = inverse(A)

        print(OUTPUT_PROMPT)
        for row in R:
            print(*row)
