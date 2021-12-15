from main import ping
import pytest



@pytest.mark.parametrize("test_input, expected", [([0], 0), ([2], 2), ([1,1,2], 2), ([1,1,2,3,3,4], 2), ([1,2,1,2], None)])
def test_ping(test_input, expected):
    assert ping(test_input) == expected

