##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields

class LegalNegotiationConcept(models.Model):

    _name = 'legal.negotiation.concept'

    name = fields.Char()
