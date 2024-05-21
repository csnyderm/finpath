import pandas as pd
#from pandas import read_csv, errors
from os import path, makedirs
from pathlib import Path
from logging import Logger
from sys import exit

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
    intake_file = str(path.dirname(path.realpath(__file__))).replace('\\', '/') # Always want to use Linux/Unix pathing. Replace otherwise.
    try:
      intake_file = intake_file[:intake_file.find('finpath')] + 'data'
      logger.warn("Warning: Data path not set in the configuration file. Adding default to configuration file.")
      # Yada yada add here
    
    except:
      logger.critical("CRITICAL ERROR: Unable to determine local path for the application. Terminating program.")
      exit(1)
    return False
  
  # Then check if the data path exists
  if not Path(data_path):
    makedirs(data_path) # Create up to the data path, if necessary.
    logger.info(f"Warning: Unable to find data path at config location: {data_path}. Creating path.")
    return False
  
  return True




def create_data_file(data_path:str, source:str, logger:Logger) -> bool:
  """Create or update the data file with the correct headers. Without proper CSV headers (columns) to parse, Pandas will error out when trying to read a csv.

  Args:
      data_path (str): The absolute path to the data directory where the files are stored.
      source (str): The kind of data source. Valid types may be expanded, but include: Income, Savings, Expenses, Debts, etc.
      logger (Logger): The existing logger set up for logging the application.
  
  Returns:
      bool: Returns true if the file is created successfully.
  """
  match source:
    case "Savings":
      pass
    case "Income":
      pass
    case "Expenses":
      pass
    case "Debts":
      pass
    case _:
      pass
  
  # Open and create file here


def load_data(data_path:str, data_sources:list, logger:Logger) -> bool | tuple:
  """Attempts to load all given data sources from the data directory.

  Args:
      data_path (str): The absolute path to the data directory where the sources are stored.
      data_sources (list): A list of all data sources to import.
      logger (Logger): The existing logger set up for logging the application.

  Returns:
      bool | tuple: Returns False if it is unable to load data. This can occur if the files need to be created. Returns a tuple of data loaded into Pandas if it successfully loaded the data.
  """
  
  
  for source in data_sources:
    current_file_path = data_path + '/' + source + '.csv'
    data = []
    
    try:
      current_file = pd.read_csv(current_file_path)
      data += current_file
    
    except FileNotFoundError:
      logger.error(f"Error: {source}.csv was not found at the data path. Creating a file with appropriate headers.")
      # Add create_data_file
      return False
    
    except pd.errors.EmptyDataError:
      logger.error(f"Error: {source}.csv was found, but it is missing the appropriate headers. Writing appropriate headers to file.")
      # Add create_data_file
      return False
    
    except Exception as e:
      logger.critical(f"CRITICAL! Error that occurred: {e}")
      exit(1)
  
  return tuple(data)