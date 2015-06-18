# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_claim(models.Model):

    """"""

    _name = 'legal.claims'

    total_claim = fields.Float(string='Total Claim')
    description = fields.Char(string='Description')
    type_claim = fields.Char(string='Type of Claim')
    category_claim = fields.Char(string='Category of claim')
    procese_id = fields.Many2one('legal.procese', string='Procese')


class legal_claim_type(models.Model):

    """"""

    _name = 'legal.claims_type'

    name = fields.Char('Name')
    procese_id = fields.Many2one('legal.procese', string='Procese')
