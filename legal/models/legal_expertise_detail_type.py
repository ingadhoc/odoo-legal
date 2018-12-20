##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields

class LegalExpertiseDetailType(models.Model):

    _name = 'legal.expertise.detail_type'

    name = fields.Char()

    expertise_type_id = fields.Many2one(
        'legal.expertise.type',
    )
