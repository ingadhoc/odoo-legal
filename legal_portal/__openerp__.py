# -*- coding: utf-8 -*-

{
    'name': 'Legal Portal',
    'version': '8.0.0.0.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
Legal Portal
============
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'legal',
        'portal'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/portal_security.xml',
        'portal_legal_view.xml',
    ],
    'installable': False,
    'auto_install': True,
    'category': 'Hidden',
}
