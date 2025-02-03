import os
import sys
import logging

# Defines the format for the log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where log files will be stored
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")

# Creates the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configures the logging settings (log level, format, and handlers)
logging.basicConfig(
    level= logging.INFO,  # Sets the minimum level of logs to be captured (INFO)
    format= logging_str,  # Specifies the log message format
    handlers=[  # Specifies where the logs will be saved and displayed
        logging.FileHandler(log_filepath),  # Saves logs to a file
        logging.StreamHandler(sys.stdout)   # Displays logs on the console
    ]
)

# Creates a logger instance
logger = logging.getLogger("cnnClassifierLogger")
