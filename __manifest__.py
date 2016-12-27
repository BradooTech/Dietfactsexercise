# -*- coding: utf-8 -*-
{
    'name': "dietfacts",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        A module of facts and foods
    """,

    'author': "Diogo from Bradoo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],
    'installable' : True,

    # always loaded
    'data': [
         'security/ir.model.access.csv',
#        'views/views.xml',
#        'views/templates.xml',
        'views/dietfacts_view.xml',
        'views/dietfacts_reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
