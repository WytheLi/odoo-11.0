#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from odoo import models, fields, api


class follower(models.Model):
    """
    关注者
    """
    _inherit = 'res.partner'
    bug_ids = fields.Many2many('bm.bug', string='bug')
