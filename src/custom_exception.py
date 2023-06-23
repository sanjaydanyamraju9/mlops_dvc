import sys


def custom_error_message(e, error_details:sys):
    _,_,exception_info = error_details.exc_info()
    line_no = exception_info.tb_lineno
    file_name = exception_info.tb_frame.f_code.co_filename
    custom_error_message = f"Error Encountered in the file {file_name} at line {line_no} and the error is {e}"
    return custom_error_message


class CustomException(Exception):
    def __init__(self, e, error_details:sys):
        super().__init__(e)
        self.error_message = custom_error_message(e,error_details)

    def __str__(self) -> str:
        return self.error_message