from suave.configuration import Configuration

class Client(object):

    def __init__(self, token: str,
                 output_format: str = 'json',
                 proxy: Dict = None,
                 config: Configuration = None):
        if config: 
            self.config = config 
        else:
            self.config = Configuration(
                token, 
                output_format,
                proxy)