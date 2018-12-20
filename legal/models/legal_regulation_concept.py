##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalRegulationConcept(models.Model):

    _name = 'legal.regulation.concept'

    name = fields.Char()
