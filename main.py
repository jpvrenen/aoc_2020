from conf import config
import os
import sys
import configparser
from modules.log_init import log_settings


# global variables
classification = 'day1'  # we may need this
script_base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
parameters = config.variables
cfg = configparser.ConfigParser()
cfg.read_string(parameters)

# logging section
logger = log_settings(script_base_dir)

# define class(es)


def main():
    pass


if __name__ == '__main__':
    main()
