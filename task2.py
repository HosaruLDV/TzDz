"Задание 2.1"


def null_driwer(list):
    for i in range(len(list) - 1):
        if list[i] == 0:
            list.append(list[i])
            list.remove(list[i])

    return list


"Задание 2.2"


def row_sum(n:int):
    prev_row: list[int] = []
    n_row: list[int] = []

    if n > 1:
        for i in range(1, n * (n - 1), 2):
            prev_row.append(i)

        for i in range(prev_row[-1] + 2, prev_row[-1] + (n * 2) + 2, 2):
            n_row.append(i)
    else:
        n_row.append(n)

    return sum(n_row)