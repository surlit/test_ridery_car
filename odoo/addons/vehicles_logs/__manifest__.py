# -*- coding: utf-8 -*-
{
    'name': "vehicles_logs",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Register logs 
    """,
    'sequence':1,
    'application':True,
    'author': "Luis Silva",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Logs',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','vehicle'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        
    ],
    
}
