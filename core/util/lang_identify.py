# -*- coding:utf-8 -*-
from re import search


class lang_identify:
    """docstring for lang_identify"""

    def __init__(self, framework, content, headers):
        self.framework = framework
        self.content = content
        self.headers = headers
        self._lang = None

    def run_crawl(self):
        for i in dir(self):
            con1 = not i.startswith("__")
            con2 = not i.endswith("__")
            con3 = i not in ("_lang", "content", "headers",
                             "framework", "get_lang", "run_crawl")
            if(con1 and con2 and con3):
                getattr(self, i)()

    def ruby(self):
        if(search(r"<a href\=\S*(\.rb|\.rhtml)", self.content)):
            self._lang = "Ruby"

    def asp(self):
        if(search(r"<a href\=\S*(\.asp)", self.content)):
            self._lang = "ASP"

    def asp_net(self):
        if(search(r"<a href\=\S*(\.aspx|\.axd|\.asx|\.asmx|\.ashx|\.asax|\.ascx|\.cshtml)", self.content)):
            self._lang = "ASP.NET"

    def cold_fusion(self):
        if(search(r"<a href\=\S*(\.cfm|\.cfml)", self.content)):
            self._lang = "ColdFusion"

    def flash(self):
        if(search(r"<a href\=\S*(\.swf)", self.content)):
            self._lang = "Flash"

    def perl(self):
        if(search(r"<a href\=\S*(\.pl|\.cgi)", self.content)):
            self._lang = "Perl"

    def python(self):
        if(search(r"<a href\=\S*(\.py)", self.content)):
            self._lang = "Python"

    def php(self):
        if(search(r"<a href\=\S*(\.php|\.php2|\.php3|\.php4|\.php5|\.phtm|\.phtml)", self.content)):
            self._lang = "PHP"

    def java(self):
        if(search(r"<a href\=\S*(\.do|\.jhtml|\.jsp|\.jspa|\.jspx|\.jws|\.wss|\.action)", self.content)):
            self._lang = "Java"

    @property
    def get_lang(self):
        return self._lang
