##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )

    @api.onchange('prosecution_id')
    def _on_change_prosecution(self):
        if self.prosecution_id:
            self.reference = ' - '.join(
                [self.prosecution_id.folder_name or '',
                 self.prosecution_id.caratula or '']
            )
