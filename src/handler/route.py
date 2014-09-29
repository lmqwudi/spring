# -*- coding: utf-8 -*-

from handler import (
    index,
    game,
    blog,
    read,
    program,
    about,
    life,
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
    (r'/blog/01', blog.OneHandler),
    (r'/blog/02', blog.TwoHandler),
]

read_handlers = [
    (r'/read', read.IndexHandler),
]

program_handlers = [
    (r'/program', program.IndexHandler),
]

about_handlers = [
    (r'/about', about.IndexHandler),
]

life_handlers = [
    (r'/life', life.IndexHandler),
]

handlers = (
    index_handlers + game_handlers
    + blog_handlers + read_handlers
    + program_handlers + about_handlers
    + life_handlers
)
