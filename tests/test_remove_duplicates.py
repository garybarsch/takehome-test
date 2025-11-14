#
# tests for takehome.remove_duplicates
#

import pytest

from takehome.remove_duplicates import remove_duplicates1, remove_duplicates2


common_params = pytest.mark.parametrize(
    "input_list, expected",
    [
        (
            [1, 1, 1, 2, 3, 4, 4, 5],
            [1, 2, 3, 4, 5],
        ),
        (
            [4, 1, 2, 1, 6, 4, 4],
            [1, 2, 4, 6],
        ),
        (
            [3, 3, 3, 3],
            [3],
        ),
        (
            [-1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6][::-1],
            [-1, 1, 2, 3, 4, 5, 6],
        ),
    ],
)


@common_params
def test_remove_duplicates1(input_list: list[int], expected: list[int]):
    assert remove_duplicates1(items=input_list) == expected


@common_params
def test_remove_duplicates2(input_list: list[int], expected: list[int]):
    assert remove_duplicates2(items=input_list) == expected
