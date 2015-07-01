# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_auxiliary(models.Model):

    """"""

    _name = 'legal.auxiliary'

    field_id = fields.Many2one(
        'legal.auxiliary.field', string="Auxiliary")
    value = fields.Char(string="Value")
    prosecution_id = fields.Many2one('legal.prosecution', string="prosecution")


class legal_auxiliary_field(models.Model):

    """"""

    _name = 'legal.auxiliary.field'

    name = fields.Char(string="Name")
