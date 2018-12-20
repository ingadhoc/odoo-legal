
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalClaimCategory(models.Model):

    _name = 'legal.claim.category'

    name = fields.Char()
