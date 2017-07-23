
import os
import logging

# database name to store biological information and coordinates of structures
DB='cellcraft'
TEST_DB='test'


current_env = os.environ.get('app_env')
root_logger = logging.getLogger()

current_env = 'test'

if current_env == 'cellcraft':
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    root_logger.setLevel(logging.INFO)


elif current_env == 'test':
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    root_logger.setLevel(logging.DEBUG)

else:
    logging.warning('Please configure a environment using now default dev environment for config')
    root_logger.setLevel(logging.DEBUG)
