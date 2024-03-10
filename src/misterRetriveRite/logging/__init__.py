import os
import sys
import logging

'''
1) configure logger with level, format, and handler
'''

log_dir = "logs"
log_file_name = "running_logs.log"
log_file_path = os.path.join(log_dir,log_file_name)
os.makedirs(log_dir, exist_ok= True)

logging_str = "[%(asctime)s,%(levelname)s,%(module)s,%(message)s]"


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_file_path),logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("misterRetriveRite")
