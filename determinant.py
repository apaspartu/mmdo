def determinant(A: list[list[float]], J: list[int], i: int) -> float:
    if len(J) == 1:
        return A[i][J[0]]
    else:
        det = 0
        for p in range(len(J)):
            j = J[p]
            K = [k for k in J if k != j]
            minor = determinant(A, K, i + 1)
            c = ((-1) ** p) * minor
            det += A[i][j] * c
        return det


if __name__ == '__main__':
    SIZE_PROMPT = 'Введіть розмір N матриці A:'
    ELEMENTS_PROMPT = 'Введіть N рядків по N елементів, розділених пробілами:'
    ERROR_PROMPT = 'Введено недостатньо елементів рядка: {} < {}'
    OUTPUT_PROMPT = 'Визначник D = {:g}'

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

        det = determinant(A, [*range(n)], 0)
        print(OUTPUT_PROMPT.format(det))
