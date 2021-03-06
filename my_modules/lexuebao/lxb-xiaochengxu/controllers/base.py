# -*- coding: utf-8 -*-
###############################################################################
#
#
#
#
#
#
###############################################################################

import json

from odoo import http, exceptions
from odoo.http import request

from .. import defs

import logging

_logger = logging.getLogger(__name__)


error_code = {
    -1: u'服务器内部错误',
    0: u'接口调用成功',
    403: u'禁止访问',
    405: u'错误的请求类型',
    501: u'数据库错误',
    502: u'并发异常，请重试',
    600: u'缺少参数',
    601: u'无权操作:缺少 token',
    602: u'签名错误',
    700: u'暂无数据',
    701: u'该功能暂未开通',
    702: u'资源余额不足',
    901: u'登录超时',
    300: u'缺少参数',
    400: u'域名错误',
    401: u'该域名已删除',
    402: u'该域名已禁用',
    404: u'暂无数据',
    10000: u'微信用户未注册'
}


class BaseController(object):

    def _check_domain(self, sub_domain):
        wxxcx_entry = request.env['wxxcx.config'].sudo().search([('sub_domain', '=', sub_domain)])
        if not wxxcx_entry:
            return self.res_err(404), None
        return None, wxxcx_entry

    def _check_user(self, sub_domain, token):
        user = request.env['wxxcx.config'].sudo().search([('sub_domain', '=', sub_domain)])
        if not user:
            return self.res_err(404), None, user

        if not token:
            return self.res_err(300), None, user

        access_token = request.env(user=1)['wxxcx.access_token'].search([
            ('token', '=', token),
            #('create_uid', '=', user.id)
        ])

        if not access_token:
            return self.res_err(901), None, user

        wechat_user = request.env(user=1)['wxxcx.user'].search([
            ('open_id', '=', access_token.open_id),
            #('create_uid', '=', user.id)
        ])

        if not wechat_user:
            return self.res_err(10000), None, user

        return None, wechat_user, user


    def res_ok(self, data=None):
        ret = {'code': 0, 'msg': 'success'}
        if data:
            ret['data'] = data
        return request.make_response(
            headers={'Content-Type': 'json'},
            data=json.dumps(ret)
        )

    def res_err(self, code, data=None):
        ret = {'code': code, 'msg': error_code[code]}
        if data:
            ret['data'] = data
        return request.make_response(json.dumps(ret))


def convert_static_link(request, html):
    base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
    return html.replace('src="', 'src="{base_url}'.format(base_url=base_url))