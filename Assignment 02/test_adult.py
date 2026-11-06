import pytest

from adult import is_adult

# Test case for age 17

def test_age_17():
    assert is_adult(17) is False
    
# Test case for age 18
def test_age_18():
    assert is_adult(18) is True

# Test case for negative age
def test_negative_age():
    with pytest.raises(ValueError):
        is_adult(-1)