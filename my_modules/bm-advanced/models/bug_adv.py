#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from odoo import models, fields, api


class BugAdvanced(models.Model):

    _inherit = 'bm.bug'

    need_time = fields.Integer('需要时间（h）')
    # 为bm.bug类的name字段增加help属性
    name = fields.Char(help='简要描述bug')
    stage_id = fields.Many2one('bm.bug.stage', '阶段')
    # 系统默认关联表名 本模型表名_关联模型表名_rel
    tag_ids = fields.Many2many('bm.bug.tag', string='标示')
    # 自定义关联表名
    # tag_ids = fields.Many2many(comodel_name='bm.bug.tag',
    #                            relation='bug_tag_rel',
    #                            column1='bug_id',
    #                            column2='tag_id',
    #                            string='标示')
    discovers = fields.Reference([('res.user', '用户'), ('res.partner', '合作伙伴')], 'bug发现者')
