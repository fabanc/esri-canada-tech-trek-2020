import logging
def dummy_function():
    logging.debug("Run into dummy function")
    return True

import logging
def dummy_error():
    raise Exception ("Run into dummy error!")
    