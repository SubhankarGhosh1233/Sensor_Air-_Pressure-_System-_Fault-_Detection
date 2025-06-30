from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os


def test_logger_and_exception():
    try:
        logging.info("starting the est_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("stopping the est_logger_and_exception")
    except Exception as e:
        logging.debug("starting the est_logger_and_exception")

        raise SensorException(e,sys)
    
if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="apsSensor",collection_name="Sensor")

    except Exception as e:
        print(e)
