# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_claim(models.Model):

    """"""

    _name = 'legal.claim'

    total = fields.Float(string='Total Claim', store=True)
    description = fields.Char(string='Description')
    category_id = fields.Many2one('legal.claim.type', string='Category')
    process_id = fields.Many2one('legal.process', string='process')


class legal_claim_type(models.Model):

    """"""

    _name = 'legal.claim.type'

    name = fields.Char('Name')
    process_id = fields.Many2one('legal.process', string='process')
