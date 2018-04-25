# -*- coding: utf-8 -*-
{
    'name': "hr_holidays_jaarvis",

    'summary': """
        this module will coontrol the information regarding jaarvis leaves""",

    'description': """
        Add some leave types according to jaarvis needs
    """,

    'author': "RohitK",
    'website': "http://www.jaarvistech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/hr_holidays_jaarvis_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

}