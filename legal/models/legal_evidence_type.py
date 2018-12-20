##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields

class LegalEvidenceType(models.Model):

    _name = 'legal.evidence.type'

    name = fields.Char('Name')
