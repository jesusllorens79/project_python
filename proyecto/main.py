# Parsing Libs
from argparse import ArgumentParser

from src.orchestrator import * 
from src.logger.logger import *
from src.settings.env_settings import * 
import logging

def main(args):

    # Loading the Environment Variables
    env_paths = LoadEnvironment()
    
    # Creating the Logger Object
    logger = LoggerMaster(log_path=env_paths.log_path,
                          logging_level=logging.DEBUG,
                          log_identifier=env_paths.log_identifier)

    # Init the logger and first message
    logger.init_logger()
    logger.first_log()

    orchestrator(args, env_paths, logger)


if __name__ == '__main__':
    
    # Instanciar el objeto ArgParser
    parser = ArgumentParser("This ETL is for teaching")

    # Añadir las reglas 
    parser.add_argument("-s", "--student", help="Student Name", required=True, type=str)
    parser.add_argument("-a", "--age", help="Student Age ", required=False, type=int)
        
    # Leer el parser
    args = parser.parse_args()
    
    main(args)