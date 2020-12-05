import logging
logger = logging.getLogger(__name__)


def read_file(d, **kwargs):
    """
    function returns list where elements are lines strips blank lines and spaces
    :param d: file to read
    :return: list where elements are lines strips blank lines and spaces
    """
    result = list()
    as_int = kwargs.get('as_int', False)
    as_lines = kwargs.get('as_lines', False)
    try:
        with open(d, 'r') as f:
            if as_lines:
                return [x.rstrip('\n') for x in f.readlines()]  # or (f.read()).split('\n')
            result = list(f.read().split())
            if as_int:
                return [int(x) for x in result]
            return result
    except FileNotFoundError as e:
        response = f"read_file: {e}"
        logger.warning(response)
        return result


def read_passwords_file(d, **kwargs):
    """
    function returns list where each element is a password string
    :param d: file to read
    :return: list where each element is a password as string
    """
    result = list()
    try:
        with open(d, 'r') as f:
            result = (f.read()).split('\n\n')
            return result
    except FileNotFoundError as e:
        response = f"read_file: {e}"
        logger.warning(response)
        return result
