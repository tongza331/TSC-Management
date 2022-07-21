# -*- coding: utf-8 -*-
{
    'name': "TSC Management",

    'summary': """
        Thai Space Consortium module for management. This will manage about Team profile,
        Organization and Careers""",

    'description': """
        This module manage four topic are:
        Team, Organization, Career includes: Job and Career
    """,

    'author': "Software engineer of Thai Space Consortium",
    'website': "https://www.narit.or.th/index.php/tsc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/TSC_Organization_views.xml',
        'views/TSC_Team_views.xml',
        'views/TSC_menu.xml',
        'views/TSC_Career_views.xml',
        'views/TSC_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}
