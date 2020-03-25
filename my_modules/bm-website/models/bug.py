#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from odoo import models, api
from odoo.exceptions import ValidationError


class Bug(models.Model):
    _inherit = 'bm.bug'

    @api.model
    def website_form_input_filter(self, request, values):
        """
        自定义表单参数验证
        :param request:
        :param values:
        :return:
        """
        print(values)
        if values.get('name'):
            values['name'] = values['name'].strip()
            if len(values['name']) < 3:
                raise ValidationError('名称长度不能少于3个字符')
        return values

    # @api.model
    # def formbuilder_whitelist(self, model, fields):
    #     """
    #     website权限
    #     :param model:
    #     :param fields:
    #     :return:
    #     """
    #     pass
