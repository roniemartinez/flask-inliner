#!/usr/bin/python
__author__ = 'Ronie Martinez'
from pynliner import Pynliner


class Inliner(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(self.after_request)

    def after_request(self, response):
        if response.mimetype == 'text/html':
            response.set_data(Pynliner().from_string(response.get_data(as_text=True)).run())
        return response
