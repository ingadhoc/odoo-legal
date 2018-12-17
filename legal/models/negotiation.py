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
        string='Concept')
    date_proposal = fields.Date(
        string='Date Proposal',
        default=date.today())
    amount = fields.Float(string='Amount')
    observations = fields.Char(string='Observations')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')


class LegalNegotiationConcept(models.Model):

    _name = 'legal.negotiation.concept'

    name = fields.Char(string='Name')
