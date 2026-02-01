# To help find the error 
import sys # For Python Intepretor

class CustomException(Exception):

    def __init__(self, message:str, error_detail:Exception=None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)
        
    
    @staticmethod 
    def get_detailed_error_message(message:str,error_detail:Exception=None):
        _, _, exc_tb = sys.exc_info()
        fileName, lineNo = exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno 

        return (
            f"{message}  | "
            f"Error : {error_detail} | "
            f"File Name : {fileName} | "
            f"Line Number : {lineNo}"
        )
    
    def __str__(self):
        return self.error_message


if __name__=='__main__':

    try:
        x=1/0
    except Exception as e:
        raise CustomException("1 divided by 0", e)