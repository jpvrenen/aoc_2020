import logging.config
import yaml


def log_settings(script_base_dir, **kwargs):
    log_name = kwargs.get('log_name', __name__)
    log_config_file = "{}/log/logging.yaml".format(script_base_dir)
    with open(log_config_file, 'r') as f:
        log_config = yaml.safe_load(f.read())
    log_config['handlers']['info_file_handler']['filename'] = "{}/log/info.log".format(script_base_dir)
    log_config['handlers']['error_file_handler']['filename'] = "{}/log/errors.log".format(script_base_dir)
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(log_name)
    return logger
