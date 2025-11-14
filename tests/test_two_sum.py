#
# tests for takehome.two_sum
#

import pytest

from takehome.two_sum import two_sum

# from takehome.two_sum import two_sum_optimized


common_params = pytest.mark.parametrize(
    "nums, target, expected",
    [
        (
            [2, 7, 11, 15],
            9,
            [0, 1],
        ),
        (
            [3, 2, 4],
            6,
            [1, 2],
        ),
    ],
)


@common_params
def test_two_sum(nums, target, expected):
    assert two_sum(nums=nums, target=target) == expected


# @common_params
# def test_two_sum_optimized(nums, target, expected):
#     assert two_sum_optimized(nums=nums, target=target) == expected
