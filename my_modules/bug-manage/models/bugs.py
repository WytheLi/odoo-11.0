#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:

from odoo import models, fields, api


class bug(models.Model):
    _name = 'bm.bug'
    _description = 'bug'
    name = fields.Char('bug简述', required=True)
    detail = fields.Text(size=150)
    is_closed = fields.Boolean('是否关闭')
    close_reason = fields.Selection([('changed', '已修改'), ('cannot', '无法修改'), ('delay', '推迟')], string='关闭理由')
    user_id = fields.Many2one('res.partner', string='责任人')
    follower_ids = fields.Many2many('res.partner', string='关注者')

    @api.multi
    def do_close(self):
        """
        关闭bug按钮
        :return:
        """
        for item in self:
            item.is_closed = True
        return True
