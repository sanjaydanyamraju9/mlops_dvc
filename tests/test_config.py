from src.custom_exception import CustomException
import pytest 
import sys



class NotInRange(Exception):
    def __init__(self, message = "Not in Range Exception"):
        self.error_msg = message 
        super().__init__(self.error_msg)

def test_generic():
    a = 2
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
        

def test_random():
    a=2
    b=2
    assert True