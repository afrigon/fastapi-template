# -*- coding: utf-8 -*-

from fastapi import FastAPI
from . import __version__
from .routes.factory import RouterFactory


class ApplicationFactory:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def create(self, debug=False, router=RouterFactory().create()):
        app = FastAPI(title=self.title,
                      description=self.description,
                      version=__version__,
                      debug=debug)

        router.register(app)

        return app
