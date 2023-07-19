
{
    'name' : 'Real-Esatate Management',
    'version' : '1.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """This is a test module
    """,
    'category': 'Category',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        "view/estate.menu.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
