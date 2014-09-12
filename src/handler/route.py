# -*- coding: utf-8 -*-

from handler import (
    index,
    game,
    blog,
    read,
)


index_handlers = [
    (r'/', index.IndexHandler),
    (r'/index', index.IndexHandler),
]


game_handlers = [
    (r'/game', game.IndexHandler),
    (r'/game/chainReaction', game.ChainHandler),
]

blog_handlers = [
    (r'/blog', blog.IndexHandler),
    (r'/blog/first', blog.FirstHandler),
]

read_handlers = [
    (r'/read', read.IndexHandler),
]

handlers = (
    index_handlers + game_handlers
    + blog_handlers + read_handlers
)
