#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from odoo import models, fields, api


class BugTag(models.Model):

    _name = 'bm.bug.tag'
    _description = 'bug标示'

    name = fields.Char('名称')
    bug_ids = fields.Many2many('bm.bug', string='bugs')
