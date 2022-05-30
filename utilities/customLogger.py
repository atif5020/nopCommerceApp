import logging


class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",  # to format logging file
                            datefmt="%d/%m/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # to print 'debug & info' in log file which are not printed in console
        return logger
