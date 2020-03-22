#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from odoo import models, fields, api


class BugWizardPlus(models.TransientModel):
    _inherit = 'bug.wizard'

    @api.multi
    def update_batch(self):
        self.ensure_one()
        vals = {}
        if self.wizard_user_id:
            vals['user_id'] = self.wizard_user_id
        vals['is_closed'] = self.new_is_closed
        if vals:
            self.bug_ids.write(vals)
        return True