import logging
import logging.config
import os
import yaml

def load_from_config(config_path):
    with open(config_path, 'r') as config:
        config_dictionary = yaml.safe_load(config.read())
        config_dictionary['logging']["handlers"]["file_handler"]["filename"] = "{0}\{1}".format(os.path.dirname(os.path.realpath(__file__)), 'sample.log')
        logging.config.dictConfig(config_dictionary['logging'])


def main():
    load_from_config(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 
            'logging_config.yaml'
        )
    )
    logging.info("Script Started")
    logging.info("Script Ended")


if __name__ == "__main__":
    main()