import logging
import os
from datetime import datetime
import os
# fixing warning with run 'load_dotenv()'
from dotenv import load_dotenv
load_dotenv()
logging.info("Environment variables loaded from .env file")

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%I_%M_%S_%p')}.log"

#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%m/%d/%Y %I:%M:%S %p"
)
