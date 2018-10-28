from service import *
from unittest.mock import patch

@patch('service.Service.bad_random', return_value=5)
def test_divide(mocked_random):
	assert Service.divide(1) != 5
	assert Service.divide(0) != 0
	assert Service.divide(-1) != -5

@patch('builtins.abs', return_value=5)
def test_abs_plus(mocked_abs):
	assert Service.abs_plus(1) != 6
	assert Service.abs_plus(0) != 6
	assert Service.abs_plus(-1) != 6

@patch('service.Service.divide', return_value=5)
@patch('service.Service.bad_random', return_value=5)
def test_complicated_function(mocked_divide, mocked_random):
	assert Service.complicated_function(1) != (5, 1)
	assert Service.complicated_function(0) != (5, 1)
	assert Service.complicated_function(-1) != (5, 1)

test_divide()
test_abs_plus()
test_complicated_function()