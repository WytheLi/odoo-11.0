# -*- coding: utf-8 -*-
{
    'name': "Bug management Website",

    'summary': """
        Bug management Website
    """,

    'description': """
        Bug management Website
    """,

    'author': "willi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bm-advanced', 'website', 'website_form'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bug_web.xml',
        'views/bug_extend.xml',
        'views/bug_templates.xml',
        'data/config_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}