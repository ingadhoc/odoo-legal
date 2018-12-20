##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class LegalRadication(models.Model):

    _name = 'legal.radication'
    _order = 'date_court desc'

    address = fields.Char(
        string='Address',
        compute='_compute_address',
    )

    judged_id = fields.Many2one(
        'legal.office',
        string='Judged',
    )

    num_case_file = fields.Char(string='Num. case file')

    date_court = fields.Date(string='Date of admission to court')

    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution',
    )

    @api.multi
    @api.depends(
        'judged_id', 'judged_id.location')
    def _compute_address(self):
        for rec in self:
            address = ''
            if rec.judged_id:
                address = rec.judged_id.location
                if rec.judged_id.address:
                    address += '-' + rec.judged_id.address
            rec.address = address
