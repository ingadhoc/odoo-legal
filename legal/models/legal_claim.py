##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalClaim(models.Model):

    _name = 'legal.claim'

    total = fields.Float(
        string='Total Claim',
        store=True,
    )
    category_id = fields.Many2one(
        'legal.claim.category',
    )
    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
