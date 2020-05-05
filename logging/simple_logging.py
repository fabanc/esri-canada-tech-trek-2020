import logging
import dummy_module
def main():
    logging.basicConfig(
        level=logging.DEBUG
        ,format='%(asctime)s-%(filename)s-Line: %(lineno)s - Function: %(funcName)s-%(levelname)s-%(message)s'
    )

    logging.info("Script Started")
    dummy_module.dummy_function()
    logging.info("Script Ended")


if __name__ == "__main__":
    main()