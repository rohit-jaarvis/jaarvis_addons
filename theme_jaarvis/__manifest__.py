# -*- coding: utf-8 -*-
{
    'name': "Theme_jaarvis",

    'summary': """this module will customize the backend theme of odoo according to jaarvis needs""",

    'description': """
        Theme jaarvis
    """,

    'author': "Rohit Kumarr",
    'website': "http://www.jaarvistech.com",
    "images" : ["theme_jaarvis/static/src/img/logo_jaarvis.png"],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','web_enterprise','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/templates.xml',
        'data/company_jaarvis.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml' ],
}