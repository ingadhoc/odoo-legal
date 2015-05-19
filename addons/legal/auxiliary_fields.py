# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_auxiliary(models.Model):

    """"""

    _name = 'legal.auxiliary'

    auxiliary_field_id = fields.Many2one(
        'legal.auxiliary_fields', string="Auxiliary")
    auxiliary_fields_value = fields.Char(string="Value")
    procese_id = fields.Many2one('legal.procese', string="Procese")


class legal_auxiliary_fields(models.Model):

    """"""

    _name = 'legal.auxiliary_fields'

    name = fields.Char(string="Name")