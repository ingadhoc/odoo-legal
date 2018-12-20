##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalAuxiliaryField(models.Model):

    _name = 'legal.auxiliary.field'

    name = fields.Char()

    department_id = fields.Many2one(
        'legal.department',
        required=True
    )
