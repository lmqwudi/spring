# -*- coding:utf-8 -*-

import os

CURRENT_DIR = os.path.dirname(__file__) or '.'
PREFIX = ''

settings = dict(
    template_path=os.path.join(CURRENT_DIR, '../../', 'templates'),
    static_path=os.path.join(CURRENT_DIR, '../../', 'static'),
    debug=True
)
