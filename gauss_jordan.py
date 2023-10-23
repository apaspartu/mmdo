from helpers import get_size, get_vector, get_matrix, Vector, Matrix


def gauss_jordan(A: Matrix, b: Vector) -> Vector:
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
    print("<< Програма для розв'язування систем лінійних рівнянь методом Гауса-Жордана >>" + '\n')

    print('Введіть розмір N матриці A:')
    n = get_size()

    print('Введіть N рядків по N елементів, розділених пробілами:')
    A = get_matrix(n, n)

    print('Введіть елементи стовпця вільних змінних, розділені пробілами:')
    b = get_vector(n)

    X = gauss_jordan(A, b)

    solution = [f'x{i + 1} = {x:zg}' for i, x in enumerate(X)]
    print("Розв'язок системи:", *solution, sep='\n')
