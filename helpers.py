from typing import TypeAlias

Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]


def get_size() -> int:
    n = int(input())
    if n <= 0:
        print('Помилка! Значення повинно бути більше нуля.')
        quit(1)
    return n


def get_vector(n: int) -> Vector:
    v = list(map(float, input().split()))
    if len(v) != n:
        print(f'Помилка! Стовпців повинно бути {n}.')
        quit(1)
    return v


def get_matrix(m: int, n: int) -> Matrix:
    A = [get_vector(n) for _ in range(m)]
    if len(A) != m:
        print(f'Помилка! Рядків повинно бути {m}.')
        quit(1)
    return A
