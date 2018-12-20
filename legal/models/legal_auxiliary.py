##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalAuxiliary(models.Model):

    _name = 'legal.auxiliary'

    field_id = fields.Many2one(
        'legal.auxiliary.field',
        string="Auxiliary",
    )
    value = fields.Char()
    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
