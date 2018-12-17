##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class StockCases(models.TransientModel):
    _name = 'legal.stock_cases'

    from_date = fields.Date(
        string="From Date",
        required=True)
    to_date = fields.Date(
        string="To Date",
        required=True)
    detail = fields.Boolean(
        string="Detail of Cases")
    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer',
        domain="[('is_lawyer','=',True)]")
    prosecution_type_id = fields.Many2one(
        'legal.prosecution_type',
        string='Type of prosecution')

    @api.multi
    def generate_report(self):
        self.ensure_one()
        return self.env['report'].with_context(
            from_date=self.from_date,
            responsible_id=self.responsible_id.id,
            prosecution_type_id=self.prosecution_type_id.id,
            to_date=self.to_date).get_action(
            self, 'legal_cases_report')
