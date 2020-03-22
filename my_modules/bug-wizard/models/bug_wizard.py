#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import logging

from odoo import models, fields, api, exceptions

_logger = logging.getLogger(__name__)


class BugWizard(models.TransientModel):
    _name = 'bug.wizard'

    bug_ids = fields.Many2many('bm.bug', string='Bug')
    new_is_closed = fields.Boolean('是否关闭')
    wizard_user_id = fields.Many2one('res.users', string='负责人')

    @api.model
    def default_get(self, fields_list):
        """
        将bug列表视图选中的记录显示在新窗口
        :param fields_list:
        :return:
        """
        defaults = super(BugWizard, self).default_get(fields_list)
        defaults['bug_ids'] = self.env.context['active_ids']
        return defaults

    @api.multi
    def update_batch(self):
        """
        批量更新
        :return:
        """
        self.ensure_one()
        if not (self.new_is_closed or self.wizard_user_id):
            raise exceptions.ValidationError("无数据需要更新")
        _logger.info('批量bug更新操作 %s' % self.bug_ids.ids)
        vals = {}
        if self.new_is_closed:
            vals['is_closed'] = self.new_is_closed
        if self.wizard_user_id:
            vals['user_id'] = self.wizard_user_id
        if vals:
            self.bug_ids.write(vals)
        return True

    @api.multi
    def count_bugs(self):
        """
        统计bug列表视图记录条数
        :return:
        """
        bug = self.env['bm.bug']
        count = bug.search_count([])
        raise exceptions.Warning('有%s条bug' % count)

    @api.multi
    def helper_form(self):
        """
        向导帮助
        :return:
        """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'
        }

    @api.multi
    def get_bugs(self):
        self.ensure_one()
        # 删选未关闭的bug
        bugs = self.env['bm.bug']
        tag_bugs = bugs.search([('is_closed', '=', False)])
        self.bug_ids = tag_bugs
        return self.helper_form()
