##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class LegalOffice(models.Model):

    _name = 'legal.office'
    _rec_name = 'display_name'

    name = fields.Char()

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True,
    )

    mail = fields.Char()

    location = fields.Char(
        required=True,
    )

    address = fields.Char()

    @api.multi
    @api.depends('name', 'location')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = ' - '.join(
                [rec.name or ' ', rec.location or ' ']
            )
