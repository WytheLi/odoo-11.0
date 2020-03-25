#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from odoo import http
from odoo.http import request
from .main import Main


class MainExtended(Main):
    @http.route()
    # @http.route(['/hello', '/hello/<name>'])
    def hello(self, name=None, **kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        return response

    @http.route('/hello-cms/<page>', auth='public')
    def hello_cms(self, page, **kwargs):
        # http://localhost:8069/hello-cms/bm-website.hello_world
        return request.render(page)
