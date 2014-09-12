# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'read/index.html',
            prefix=PREFIX
        )
