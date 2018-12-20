##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalPart(models.Model):

    _name = 'legal.part'

    age = fields.Integer()

    contact = fields.Char()

    dni = fields.Integer()

    role_id = fields.Many2one(
        'legal.role',
    )

    lawyer_id = fields.Many2one(
        'res.partner',
        domain="[('is_lawyer','=',True)]",
        context={'default_is_lawyer': True},
    )

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
