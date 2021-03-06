# -*- coding: utf-8 -*-

try:
    from urllib import parse as urlparse
    from urllib.parse import quote
except ImportError:
    import urlparse as urlparse
    from urllib import quote

import re
from socket import gethostbyname, gethostbyaddr


class urlib:
    """docstring for urlib"""

    def __init__(self, url):
        self.url = url

    def join(self, urjoin):
        return urlparse.urljoin(self.url, urjoin)

    def parse(self):
        return urlparse.urlparse(self.url)

    def unparse(self, urparse):
        return urlparse.urlunparse(urparse)

    def sub_service(self, serv):
        serv = re.sub(r"://", '', serv)
        urparse = re.split(r"://", self.url)
        if(len(urparse) == 2):
            del urparse[0]
            if(serv != ''):
                url = "%s://%s" % (serv, "".join(urparse))
            else:
                url = ''.join(urparse)
        else:
            url = "%s://%s" % (serv, urparse[0])
        return url

    def quote(self):
        return quote(self.url)

    def unquote(self):
        return urlparse.unquote(self.url)

    @property
    def get_ip(self):
        return gethostbyname(self.parse().netloc)

    @property
    def get_host(self):
        return gethostbyaddr(self.parse().netloc)[0]

    @property
    def get_scheme(self):
        return self.parse().scheme

    @property
    def get_netloc(self):
        return self.parse().netloc

    @property
    def get_path(self):
        return self.parse().path

    @property
    def get_query(self):
        return self.parse().query

    @property
    def get_params(self):
        return self.parse().params

    @property
    def get_fragment(self):
        return self.parse().fragment
