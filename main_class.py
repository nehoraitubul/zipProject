import zipfile
from abc import ABC, abstractmethod

class Main(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create(self, *args, compress=False, compress_level=None, store_path='default'):
        pass

    @abstractmethod
    def extract(self, *args):
        pass

