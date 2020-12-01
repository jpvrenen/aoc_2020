def read_file(d, log, **kwargs):
    """
    function returns list where elements are lines strips blank lines and spaces
    :param d: file to read
    :param log: logger
    :return: list where elements are lines strips blank lines and spaces
    """
    result = list()
    as_int = kwargs.get('as_int', False)
    try:
        with open(d, 'r') as f:
            # return list(f.readlines())
            result = list(f.read().split())
            if as_int:
                return [int(x) for x in result]
            return result
    except FileNotFoundError as e:
        response = f"read_file: {e}"
        log.warning(response)
        return result
