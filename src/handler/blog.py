# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/index.html',
            prefix=PREFIX
        )


class FirstHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/first.html',
            prefix=PREFIX
        )
       

class Al1Handler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'blog/al_1.html',
            prefix=PREFIX
        )
