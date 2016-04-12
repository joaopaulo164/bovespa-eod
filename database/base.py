# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from . import initial_config
import logging

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


class DaoBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, database_name, settings):
        self.db = initial_config(settings)
        self.database_name = database_name

    @abstractmethod
    def get_cursor(self): pass

    @abstractmethod
    def insert(self, insert_str, value_str): pass

    @abstractmethod
    def insert_many(self, insert_str, values=[]): pass
