import configparser
import logging
import platform
import sys


class LoadEnvironment:

    def __init__(self):
        try:

            self.config = None

            if platform.system() == "Linux":
                print("[INFO] Running the ELT from Linux System")
                root_dir = "./config"
                config_file = root_dir + "/config.ini"
            else:
                print("[INFO] Running the ELT from Windows System")
                root_dir = ".\\config"
                config_file = root_dir + "\\config.ini"

            self.config = configparser.ConfigParser()
            self.config.sections()
            self.config.read(config_file)

            # Logger Info
            self.log_path = self.config["LOGGING"]["LOG_PATH"]
            self.log_level = self.config["LOGGING"]["LOG_LEVEL"]
            self.log_identifier = self.config["LOGGING"]["LOG_IDENTIFIER"]

            # Input Files
            self.input_files = self.config["INPUT_FILES"]["DATA_EXAMPLE"]

            # Output Files
            self.output_files = self.config["OUTPUT_FILES"]["OUTPUT_CSV"]

    
        except Exception as err:
            print("\n Load Environment function Error ({}".format(err) + ")")
            sys.exit(-1)