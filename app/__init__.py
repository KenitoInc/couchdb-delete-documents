from os import path, remove
import logging
import logging.config
import json

from .couch import DeleteDocuments

# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile("delete.log"):
    remove("delete.log")

with open("delete_logging_config.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Log that the logger was configured
logger = logging.getLogger(__name__)
logger.info('Completed configuring logger()!')