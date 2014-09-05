# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print 'prefix:', PREFIX
        self.render(
            'index.html',
            prefix=PREFIX
        )
