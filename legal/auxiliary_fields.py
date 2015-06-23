# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_auxiliary(models.Model):

    """"""

    _name = 'legal.auxiliary'

    field_id = fields.Many2one(
        'legal.auxiliary.field', string="Auxiliary")
    value = fields.Char(string="Value")
    process_id = fields.Many2one('legal.process', string="Process")


class legal_auxiliary_field(models.Model):

    """"""

    _name = 'legal.auxiliary.field'

    name = fields.Char(string="Name")
