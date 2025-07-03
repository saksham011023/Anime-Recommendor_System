import traceback
import sys

class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # if the exception is already in the Exception class this method automatically handles it without creating our own CustomExceptions.

        self.error_message=self.get_detailed_error_message(error_message,error_detail)

    @staticmethod
    def get_detailed_error_message(error_message,error_detail:sys):
        _,_,exc_tb=traceback.sys.exc_info()  # it return 3 values but we are only concerned with the last tracback value.
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno

        return f"Error occured in {file_name} , Line {line_number} : {error_message}"
    
    def __str__(self): #gives text format of error message.
        return self.error_message