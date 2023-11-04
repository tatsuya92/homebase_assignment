import logging

class ETLLogger:

    def __init__(self, log_file='logs/etl.log', log_level=logging.INFO, streaming: bool = False):
        # init log
        self.logger = logging.getLogger('etl_loggger')
        self.logger.setLevel(log_level)
        # formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        # log to file
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        # streaming log
        streaming_handler = logging.StreamHandler()
        streaming_handler.setFormatter(formatter)
        self.logger.addHandler(streaming_handler)

    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    