#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/hello-world', auth='public')
    def hello_world(self):
        return ('<h1>Hello world!</h1>')

    # @http.route('/hello', auth='public')
    # def hello(self):
    #     # render('模块名.视图模板id')
    #     return request.render('bm-website.hello_world')

    @http.route('/hello', auth='public', website=True)
    def hello(self):
        return request.render('bm-website.hello_world')

    @http.route('/bugs', auth='user', website=True)
    def bugs(self, **kwargs):
        """
        响应bug列表数据

        若auth='public'，不需要身份验证，可以访问的资源有限；
        request.env['bm.bug'].sudo(),
        使用sudo()模型方法，可以将安全上下文更改为Admin用户，
        从而提升业务实现的便利
        :param kwargs:
        :return:
        """
        bugs = request.env['bm.bug'].search([])
        return request.render('bm-website.bug_list', {'bugs': bugs})

    @http.route('/bug/<model("bm.bug"):bug>', auth='user', website=True)
    def bug_detail(self, bug, **kwargs):
        """

        :param bug:
        :param kwargs:
        :return:
        """
        return request.render('bm-website.bug_detail', {'bug': bug})

    @http.route('/bug/add', auth='user', website=True)
    def add_bug(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'bm-website.add_bug', {'users': users}
        )
