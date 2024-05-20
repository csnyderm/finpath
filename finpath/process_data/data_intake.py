import pandas as pd
from os import path, makedirs
from pathlib import Path
from logging import Logger
import sys

def is_data_path(data_path:str, logger:Logger) -> bool:
  """Verifies there is a data path at the current application location. 
  If the path is not set in the config, it will find the default path based on the application folder (finpath).
  If the path does not exist, it creates the path and notes it in the configuration file if not already set.
  

  Args:
      data_path (str): The absolute path to where the local files for data storage are meant to be kept.
      logger (Logger): The existing logger set up for logging the application.

  Returns:
      bool: Utilizes the path in the config file
        False if the data path does not exist, or a critical error occurs.
        True if the data path already exists.
  """
  
  # First check if the data path actually exists
  if not data_path:
    
    # If not, try to find it from "finpath" as the application folder name.
    intake_file = str(path.dirname(path.realpath(__file__)))
    try:
      intake_file = intake_file[:intake_file.find('finpath')] + 'data'
      logger.warn("Warning: Data path not set in the configuration file. Adding default to configuration file.")
      # Yada yada add here
    
    except:
      logger.critical("CRITICAL ERROR: Unable to determine local path for the application. Terminating program.")
      sys.exit(1)
    return False
  
  # Then check if the data path exists
  if not Path(data_path):
    makedirs(data_path) # Create up to the data path, if necessary.
    logger.info(f"Warning: Unable to find data path at config location: {data_path}. Creating path.")
    return False
  
  return True