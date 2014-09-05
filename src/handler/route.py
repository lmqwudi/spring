# -*- coding: utf-8 -*-

from handler import (
    index,
)


index_handlers = [
    (r'/index', index.IndexHandler),
]

handlers = (
    index_handlers
)
