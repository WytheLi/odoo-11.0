# -*- coding: utf-8 -*-
{
    'name': "bm管理系统 plus",

    'summary': """
        管理项目测试过程中发现的bug
    """,

    'description': """
        管理项目测试过程中发现的bug
    """,

    'author': "willi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bug-manage', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs_adv.xml',
        'views/bugs_stage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}