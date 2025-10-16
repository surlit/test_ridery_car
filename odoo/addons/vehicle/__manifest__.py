# -*- coding: utf-8 -*-
{
    'name': "vehicle",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Luis Silva",
    'website': "",
    'sequence':1,
    'application':True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Register',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'views/views.xml',
        'views/res_partner_customizer.xml',
        'views/vehicle_modal.xml',        
        'data/vehicle_sequence.xml',        
        
    ],
    
}
