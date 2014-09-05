# -*- coding: utf-8 -*-

from handler import (
    index,
    game,
)


index_handlers = [
    (r'/', index.IndexHandler),
    (r'/index', index.IndexHandler),
]


game_handlers = [
    (r'/game', game.IndexHandler),
    (r'/game/chainReaction', game.ChainHandler),
]

handlers = (
    index_handlers + game_handlers
)
