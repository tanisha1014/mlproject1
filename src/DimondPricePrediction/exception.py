import sys
import traceback


##in which script or file and line im getting the error
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message
        self.error_details = error_details
        _,_,exc_tb=error_details.exc_info() ##this exc method will give us the detail regarding the error
    ## detail about the execution(excution traceback,,traceback means line by line execution)
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename ## we will get line no and the filenmae
        

    def __str__(self):#3(getting the message ,,string representation of the object)
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))
        
if __name__=="__main__":
    try:

        a=1/0 ## will raise an error
    except Exception as e:  
        raise CustomException(e,sys)      