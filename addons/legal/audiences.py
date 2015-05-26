# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_audiences(models.Model):

    """"""

    _name = 'legal.audiences'

    description = fields.Char(string='Description')
    date = fields.Date(string='Date')
    procese_id = fields.Many2one('legal.procese', string='Procese')
