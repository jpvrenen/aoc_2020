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
                return list(f.readlines())
            result = list(f.read().split())
            if as_int:
                return [int(x) for x in result]
            return result
    except FileNotFoundError as e:
        response = f"read_file: {e}"
        logger.warning(response)
        return result
