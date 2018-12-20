##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields
from datetime import date


class LegalNegotiation(models.Model):

    _name = 'legal.negotiation'

    concept_id = fields.Many2one(
        'legal.negotiation.concept',
    )

    date_proposal = fields.Date(
        default=date.today(),
    )

    amount = fields.Float()

    observations = fields.Char()

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
