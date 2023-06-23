import sys
from src.custom_exception import CustomException

try:
    b = 2/0
except Exception as e:
    raise CustomException(e,sys)