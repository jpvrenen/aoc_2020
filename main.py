from conf import config
import os
import sys
import configparser
from modules.log_init import log_settings
from modules.helpers import read_file
from day1.helpers import subtract_and_find
from day1.helpers import multiply_nrs


# global variables
general = 'general'
day = 'day1'  # we may need this
script_base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
parameters = config.variables
cfg = configparser.ConfigParser()
cfg.read_string(parameters)
log_name = cfg[general]['log_name']

# logging section
logger = log_settings(script_base_dir, log_name=log_name)

# define class(es)


def main():
    pass


if __name__ == '__main__':
    # main()
    print(multiply_nrs(subtract_and_find(2020, read_file(f"{day}/numbers", logger, as_int=True))))
