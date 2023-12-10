import logging
import sys
import os
from pathlib import Path

log_str = "[%(asctime)s: %(module)s %(levelname)s: %(message)s]"
log_dir = "logs"
log_name = "running_logs.log"
log_path = os.path.join(log_dir,log_name)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = log_str,
    handlers = [
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]

)
logger = logging.getLogger("cnnClassifierLogger")