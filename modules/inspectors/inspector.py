import logging


class AbstractInspector:

    def __init__(self, name):
        logging.basicConfig(level='INFO', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        self.__inspector_name = name
        logging.info("{} started...".format(self.__inspector_name))

    def inspect(self) -> dict:
        raise NotImplementedError

    @property
    def inspector_name(self):
        return self.__inspector_name
