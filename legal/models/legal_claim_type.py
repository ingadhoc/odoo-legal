
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalClaimType(models.Model):

    _name = 'legal.claim.type'

    name = fields.Char()

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
