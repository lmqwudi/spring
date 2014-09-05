# -*- coding:utf-8 -*-

import tornado.web
from conf.config import PREFIX


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'game/index.html',
            prefix=PREFIX
        )


class ChainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'game/chainReaction/game.html',
            prefix=PREFIX
        )
