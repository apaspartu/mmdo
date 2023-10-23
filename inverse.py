from helpers import get_size, get_matrix, Matrix


def inverse(A: Matrix) -> Matrix:
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
    print('<< Програма для знаходження оберненої матриці >>' + '\n')

    print('Введіть розмір N матриці A:')
    n = get_size()

    print('Введіть N рядків по N елементів, розділених пробілами:')
    A = get_matrix(n, n)

    R = inverse(A)

    print('Обернена матриця:')
    for row in R:
        print(*(f'{i:.3f}' for i in row))
