import datetime
import logging
import sys

class LoggerMaster:

    def __init__(self, log_path, logging_level, log_identifier):

        self.log_path = log_path
        self.logging_level = logging_level
        self.log_identifier = log_identifier
        self.logger = None
   
    # Setup a Logger
    def init_logger(self):
        """
            Function to activate the event logger in both console and File
        """
        try:

            logger = logging.getLogger(self.log_identifier)
            
            logger.setLevel(self.logging_level)

            file_handler = logging.FileHandler(self.log_path +
                                               datetime.date.today().strftime('%Y%m%d') +
                                               '_' + self.log_identifier +
                                               '_ETL.log', mode='w')

            file_handler.setLevel(self.logging_level)

            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(self.logging_level)

            # Create the formatter and add it to the handlers
            formatter = logging.Formatter('[%(asctime)s] *||* %(levelname)s *||* (%(filename)s:%(lineno)s) *||* %(message)s',
                                          datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            self.logger = logger

        except Exception as err:
            print("\n Init Logger Error ({}".format(err) + ")")
            sys.exit(-1)
    

    def first_log(self):
        try:
            self.logger.info("*********** Start Execution ************* \n")
            self.logger.info("Execution Start")
            self.logger.info("Type of file to be processed: %s")

        except Exception as err:
            self.logger.log(logging.ERROR, "\n First_log Error ({}".format(err) + ")")
            sys.exit(-1)