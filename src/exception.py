#Exception handling is done here

import sys  # All the exception occurence , the sys library will have the information/ sys module in python provides various functions and variables that are used to manipulate different parts of the Python Runtime environment
import logging
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()    #the third parameter from .exc_info will provide which file,line no the exception has occured
    
    file_name = exc_tb.tb_frame.f_code.co_filename  #the file name is retrieved from the exc_tb
    
    error_message = "Error occured in python script name [{0}]  line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message =error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a= 1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
    

""" 
sample executed exceptional handling from above with output shown in below comment

Traceback (most recent call last):
  File "src/exception.py", line 25, in <module>
    a= 1/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "src/exception.py", line 28, in <module>
    raise CustomException(e,sys)
__main__.CustomException: Error occured in python script name [src/exception.py]  line number [25] error message[division by zero]"""



''' The lines from 5 to 12 where a function is created, which gives how the message should look like, with respect to Custom Exception (Line15)-We create our own CustomException inherited
from Exception 

In line 16 to 18 - overridden the init method

In line 20 the return staement - prints statement is going to print the error message'''