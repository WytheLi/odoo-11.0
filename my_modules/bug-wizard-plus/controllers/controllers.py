# -*- coding: utf-8 -*-
from odoo import http

# class Bug-wizard-plus(http.Controller):
#     @http.route('/bug-wizard-plus/bug-wizard-plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug-wizard-plus/bug-wizard-plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug-wizard-plus.listing', {
#             'root': '/bug-wizard-plus/bug-wizard-plus',
#             'objects': http.request.env['bug-wizard-plus.bug-wizard-plus'].search([]),
#         })

#     @http.route('/bug-wizard-plus/bug-wizard-plus/objects/<model("bug-wizard-plus.bug-wizard-plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-wizard-plus.object', {
#             'object': obj
#         })