# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_claim(models.Model):

    """"""

    _name = 'legal.claims'

    date_of_the_claim = fields.Date(string='Date of the claim')
    total_claim = fields.Float(string='Total Claim')
    budget_for_coasts = fields.Float(string='Budget For Coasts')
    procese_id = fields.Many2one('legal.procese', string='Procese')
