from helpers import get_size, get_matrix, Matrix


def determinant(A: Matrix) -> float:
    n = len(A)
    B = [[A[i][j] for j in range(n)] for i in range(n)]
    d = 1
    for i in range(n):
        k = B[i][i]
        if k == 0:
            k = k + 0.000001
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
    print('<< Програма для знаходження визначника матриці >>' + '\n')

    print('Введіть розмір N матриці A:')
    n = get_size()

    print('Введіть N рядків по N елементів, розділених пробілами:')
    A = get_matrix(n, n)

    det = determinant(A)

    print(f'Визначник: D = {det:zg}')
