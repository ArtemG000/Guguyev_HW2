def count_gold(pyramid: list[list[int]]) -> int:
    # replace this for solution
    pyramid_reversed = pyramid[::-1]
    for ind, level in enumerate(pyramid_reversed[:-1]):
        for i, path in enumerate(level[:-1]):
            pyramid_reversed[ind + 1][i] += max(path, level[i + 1])
    print(pyramid_reversed)
    return int(*pyramid_reversed[-1])

print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)

# These "asserts" are used for self-checking
assert (
        count_gold(
            [
                [1],
                [2, 3],
                [3, 3, 1],
                [3, 1, 5, 4],
                [3, 1, 3, 1, 3],
                [2, 2, 2, 2, 2, 2],
                [5, 6, 4, 5, 6, 4, 3],
            ]
        )
        == 23
)
assert (
        count_gold(
            [
                [1],
                [2, 1],
                [1, 2, 1],
                [1, 2, 1, 1],
                [1, 2, 1, 1, 1],
                [1, 2, 1, 1, 1, 1],
                [1, 2, 1, 1, 1, 1, 9],
            ]
        )
        == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
        count_gold(
            [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
        )
        == 35
)
assert (
        count_gold(
            [
                [4],
                [3, 0],
                [5, 1, 1],
                [2, 0, 2, 0],
                [1, 1, 1, 8, 3],
                [5, 3, 4, 8, 2, 8],
                [1, 0, 5, 0, 4, 3, 1],
            ]
        )
        == 30
)