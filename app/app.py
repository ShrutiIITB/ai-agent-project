import subprocess 
import threading
import time 
from dotenv import load_dotenv

from app.utlis.common_exception import CustomException
from app.utlis.logger import get_logger 

logger = get_logger(__name__) 

load_dotenv()

def run_backend():
    try:
        logger.info('Starting Agent API Service')
        subprocess.run(['uvicorn' , 'app.backend.api:app', '--host', '127.0.0.1', '--port', '8080'], check=True)
    
    except CustomException as e:
        logger.error('Problem with Backend')
        raise CustomException('Failed to Start Backend', e)
    
def run_frontend():
    try:
        logger.info('Starting UI Service')
        subprocess.run(['streamlit', 'run', 'app/frontend/colored_ui.py'], check=True)

    except CustomException as e:
        logger.error('Problem with Frontend')
        raise CustomException('Failed to Start UI', e)

if __name__ == '__main__':

    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)
        run_frontend()
    
    except CustomException as e :
        logger.exception(f"CustomException occured : {str(e)}")
        raise CustomException('Failed to start Application', str(e))
