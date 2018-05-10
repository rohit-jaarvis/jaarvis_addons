# -*- coding: utf-8 -*-
{
    'name': "hr_jaarvis",

    'summary': """customize hr modules according to jaarvis needs""",

    'description': """
        Customize hr module according to jaarvis needs 
        
    """,

    'author': "Rohit Kumar",
    'website': "http://www.jaarvistech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_contract_salary'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/hr_jaarvis_data.xml',
        'views/hr_jaarvis.xml'
    ],
    # only loaded in demonstration mode
}