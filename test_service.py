from service import *
from unittest.mock import patch


@patch('service.Service.bad_random', return_value=5)
def test_divide(mocked_random):
    service = Service()

    assert service.divide(1) == 5
    assert service.divide(0) == 0
    assert service.divide(-1) == -5


@patch('builtins.abs', return_value=5)
def test_abs_plus(mocked_abs):
    service = Service()
    assert service.abs_plus(1) == 6
    assert service.abs_plus(0) == 6
    assert service.abs_plus(-1) == 6
    assert service.abs_plus('hello') == 6


@patch('service.Service.divide', return_value=5)
@patch('service.Service.bad_random', return_value=5)
def test_complicated_function(mocked_divide, mocked_random):
    service = Service()
    assert service.complicated_function(1) == (5, 1)
    assert service.complicated_function(0) == (5, 1)
    assert service.complicated_function(-1) == (5, 1)


test_divide()
test_abs_plus()
test_complicated_function()
