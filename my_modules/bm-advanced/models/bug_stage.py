#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from odoo import models, fields, api


class BugStage(models.Model):
    _name = 'bm.bug.stage'
    _description = 'bug阶段'
    _order = 'sequence,name'

    name = fields.Char('名称')
    desc_detail = fields.Text('描述')
    status = fields.Selection([('waiting', '未开始'),
                               ('doing', '进行中'),
                               ('closed', '关闭'),
                               ('reword', '重测未通过')], '状态')
    document = fields.Html('文档')
    sequence = fields.Integer('Sequence')
    percent_pro = fields.Float('进度', (3, 2))
    deadline = fields.Date('截止日期')
    create_on = fields.Datetime('创建时间',
                                default=lambda self: fields.Datetime.now())
    delay = fields.Boolean('是否延误')
    image = fields.Binary('图片')
    bug_ids = fields.One2many('bm.bug', 'stage_id', string='bugs')
