# -*- coding: utf-8 -*-

import os
from app import ApplicationFactory

title = 'API'
description = ''
debug = os.environ.get('APP_DEBUG') or False

app = ApplicationFactory(title, description).create(debug=debug)
