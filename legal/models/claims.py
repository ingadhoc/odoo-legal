# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalClaim(models.Model):

    _name = 'legal.claim'

    total = fields.Float(
        string='Total Claim',
        store=True)
    category_id = fields.Many2one(
        'legal.claim.category',
        string='Category')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')


class LegalClaimType(models.Model):

    _name = 'legal.claim.type'

    name = fields.Char('Name')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')


class LegalClaimCategory(models.Model):

    _name = 'legal.claim.category'

    name = fields.Char('Name')