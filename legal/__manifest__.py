##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Legal',
    'version': '11.0.1.1.0',
    'category': 'base.module_category_knowledge_management',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'calendar',
        'portal',
        'report_aeroo',
        'l10n_ar_aeroo_base',
        'account'
    ],
    'data': [
        'security/legal_group.xml',
        'security/ir.model.access.csv',
        'view/legal_menuitem.xml',
        'view/res_partner_view.xml',
        'view/prosecution_view.xml',
        'view/claims_view.xml',
        'view/radication_view.xml',
        'view/auxiliary_field_view.xml',
        'view/models_view.xml',
        'view/office_view.xml',
        'view/regulation_view.xml',
        'view/news_view.xml',
        'view/parts_view.xml',
        'view/evidence_view.xml',
        'view/negotiation_view.xml',
        'view/claims_type_view.xml',
        'view/responsibility_view.xml',
        'view/news_view.xml',
        'view/calendar_view.xml',
        'view/expertise_view.xml',
        'view/expertise_detail_view.xml',
        'view/expertise_detail_type_view.xml',
        'view/account_invoice_view.xml',
        'data/prosecution_data.xml',
        'wizard/stock_case_wizard.xml',
        'report/legal_report.xml'
    ],
    'demo': [
        'data/demo/res.partner.csv',
        'data/demo/res_users.xml',
        'data/demo/res_company.xml',
        'data/demo/legal.office.csv',
        'data/demo/legal.expertise.type.csv',
        'data/demo/legal.expertise.detail_type.csv',
        'data/demo/legal.status.csv',
        'data/demo/legal.substate.csv',
        'data/demo/legal.office.csv',
        'data/demo/legal.role.csv',
        'data/demo/legal.claim.type.csv',
        'data/demo/legal.claim.category.csv',
        'data/demo/legal.prosecution_type.csv',
        'data/demo/legal.department.csv',
        'data/demo/legal.prosecution.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
