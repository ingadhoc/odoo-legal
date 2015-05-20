# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_regulation(models.Model):

    """"""

    _name = 'legal.regulation'

    date_regulation = fields.Datetime(string="Date of the regulation")
    amount_regulation = fields.Float(string="Amount of regulation")
    procese_id = fields.Many2one('legal.procese', string='Procese')
