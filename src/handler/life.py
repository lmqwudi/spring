# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'life/one.html',
            prefix=PREFIX
        )
