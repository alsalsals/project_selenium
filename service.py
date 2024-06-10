import logging


class Service:
    logger = None

    @staticmethod
    def setup_logging():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        Service.logger = logging.getLogger("CustomLogger")
