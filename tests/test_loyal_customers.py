#
# tests for takehome.loyal_customers
#
import pytest

from takehome.loyal_customers import find_loyal_customers

common_params = pytest.mark.parametrize(
    "log_data, expected",
    [
        (
            (
                "day1 c888 page1\n"
                "day1 c775 page2\n"
                "day1 c111 page1\n"
                "day1 c233 page2\n"
                "day1 c410 page2\n"
                "day1 c111 page1\n"
                "day2 c111 page2\n"
                "day2 c913 page2\n"
                "day2 c233 page1\n"
                "day2 c775 page2\n"
                "day2 c913 page2\n"
            ),
            ["c111", "c233"],
        ),
        (
            (
                "day1 c888 page1\n"
                "day1 c775 page2\n"
                "day1 c410 page2\n"
                "day1 c888 page1\n"
                "day1 c775 page2\n"
                "day1 c410 page2\n"
                "day1 c888 page1\n"
                "day2 c775 page2\n"
                "day2 c775 page2\n"
                "day2 c888 page1\n"
                "day2 c775 page2\n"
                "day2 c913 page2\n"
            ),
            [],
        ),
    ],
)


@common_params
def test_find_loyal_customers(log_data: str, expected: list[str]):
    assert find_loyal_customers(log_data) == expected
