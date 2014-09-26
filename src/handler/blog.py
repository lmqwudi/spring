# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/index.html',
            prefix=PREFIX
        )


class OneHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/1.html',
            prefix=PREFIX
        )


class TwoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/2.html',
            prefix=PREFIX
        )
