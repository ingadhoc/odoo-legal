##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalExpertiseDetail(models.Model):

    _name = 'legal.expertise.detail'

    detail_type_id = fields.Many2one(
        'legal.expertise.detail_type',
    )

    value = fields.Char()

    expertise_id = fields.Many2one(
        'legal.expertise',
    )
