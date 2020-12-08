from conf import config
import os
import sys
import configparser
from modules.log_init import log_settings
from day7.helpers import part_one
from day7.helpers import part_two


# global variables
general = 'general'
day = 'day7'  # we may need this
script_base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
parameters = config.variables
cfg = configparser.ConfigParser()
cfg.read_string(parameters)
log_name = cfg[general]['log_name']

# logging section
logger = log_settings(script_base_dir, log_name=log_name)

# define class(es)


def main():
    part_one(script_base_dir, day)
    part_two(script_base_dir, day)


if __name__ == '__main__':
    main()
