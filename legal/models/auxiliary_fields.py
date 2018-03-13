# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalAuxiliary(models.Model):

    _name = 'legal.auxiliary'

    field_id = fields.Many2one(
        'legal.auxiliary.field',
        string="Auxiliary")
    value = fields.Char(string="Value")
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string="prosecution")


class LegalAuxiliaryField(models.Model):

    _name = 'legal.auxiliary.field'

    name = fields.Char(string="Name")
    department_id = fields.Many2one(
        'legal.department',
        string='Department',
        required=True
    )
