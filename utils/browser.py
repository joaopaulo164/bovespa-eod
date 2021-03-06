# -*- coding: utf-8 -*-
import requests
import time
from config import LoggerLoader

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class Browser(object):

    """
        A web session to navigate on the Bovespa website, with cookies.
    """

    def __init__(self):

        headers = {
                'Host': 'www.bmfbovespa.com.br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4,en-CA;q=0.2',
                'DNT': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(headers)

    def get_page(self, url):
        """
            Return a HTML web page from the param
        :param url: str
        :return: HTML web site
        :raise e: If a error on process
        """
        try:
            for tries in xrange(0, 4):
                resp = self.session.get(url)
                if resp.status_code == requests.codes.ok:
                    return resp.content
                else:
                    time.sleep(10)
            raise Exception('The uri {uri} can not be downloaded. Check the your uri and try again.'.format(uri=url))

        except Exception, e:
            logger.error(e)
            raise e
