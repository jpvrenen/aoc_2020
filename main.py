from conf import config
import os
import sys
import configparser
from modules.log_init import log_settings
from day9.helpers import part_one
from day9.helpers import part_two


# global variables
general = 'general'
day = 'day9'  # we may need this
script_base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
parameters = config.variables
cfg = configparser.ConfigParser()
cfg.read_string(parameters)
log_name = cfg[general]['log_name']

# logging section
logger = log_settings(script_base_dir, log_name=log_name)

# define class(es)


def main():
    print(f"==============")
    print(f"{day}: part 1")
    part_one(script_base_dir, day)
    print(f"==============")
    print(f"{day}: part 2")
    part_two(script_base_dir, day)


if __name__ == '__main__':
    main()
