# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_claim(models.Model):

    """"""

    _name = 'legal.claim'

    total = fields.Float(string='Total Claim', store=True)
    category_id = fields.Many2one('legal.claim.category', string='Category')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')


class legal_claim_type(models.Model):

    """"""

    _name = 'legal.claim.type'

    name = fields.Char('Name')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')


class legal_claim_category(models.Model):

    """"""

    _name = 'legal.claim.category'

    name = fields.Char('Name')
