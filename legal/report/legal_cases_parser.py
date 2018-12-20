##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class Parser(models.AbstractModel):
    _inherit = 'report.report_aeroo.abstract'
    _name = 'report.legal_cases_report_parser'

    @api.model
    def aeroo_report(self, docids, data):
        if not data:
            data = {}

        self.from_date = context.get('from_date', False)
        self.to_date = context.get('to_date', False)
        self.detail = context.get('detail', False)
        self.responsible_id = context.get('responsible_id', False)
        self.prosecution_type_id = context.get('prosecution_type_id', False)

        data.update({
            'config': self.config,
            'show_cases_initial': self.show_cases_initial,
            'show_cases_new': self.show_cases_new,
            'show_cases_close': self.show_cases_close,
            'show_cases_re_open': self.show_cases_re_open,
            })

        return super(Parser, self).aeroo_report(docids, data)

    def show_cases_initial(self):

        prosecution_obj = self.pool.get('legal.prosecution')
        domain = [('opening_date_folder', '<=', self.from_date),
                  ('re_opening_date_folder', '=', False)]
        if self.responsible_id:
            domain.append(('responsible_id', '=', self.responsible_id))
        if self.prosecution_type_id:
            domain.append(
                ('prosecution_type_id', '=', self.prosecution_type_id))
        cases = prosecution_obj.search(
            self.cr, self.uid, domain)
        return prosecution_obj.browse(self.cr, self.uid, cases)

    def show_cases_new(self):
        prosecution_obj = self.pool.get('legal.prosecution')
        domain = [('opening_date_folder', '>=', self.from_date),
                  ('opening_date_folder', '<=', self.to_date)]
        if self.responsible_id:
            domain.append(('responsible_id', '=', self.responsible_id))
        if self.prosecution_type_id:
            domain.append(
                ('prosecution_type_id', '=', self.prosecution_type_id))
        cases = prosecution_obj.search(
            self.cr, self.uid, domain)
        return prosecution_obj.browse(self.cr, self.uid, cases)

    def show_cases_close(self):
        prosecution_obj = self.pool.get('legal.prosecution')
        domain = [('close_date_folder', '>=', self.from_date),
                  ('opening_date_folder', '<=', self.to_date),
                  ('re_opening_date_folder', '=', False)]
        if self.responsible_id:
            domain.append(('responsible_id', '=', self.responsible_id))
        if self.prosecution_type_id:
            domain.append(
                ('prosecution_type_id', '=', self.prosecution_type_id))
        cases = prosecution_obj.search(
            self.cr, self.uid, domain)
        return prosecution_obj.browse(self.cr, self.uid, cases)

    def show_cases_re_open(self):
        prosecution_obj = self.pool.get('legal.prosecution')
        domain = [('re_opening_date_folder', '>=', self.from_date),
                  ('re_opening_date_folder', '<=', self.to_date)]
        if self.responsible_id:
            domain.append(('responsible_id', '=', self.responsible_id))
        if self.prosecution_type_id:
            domain.append(
                ('prosecution_type_id', '=', self.prosecution_type_id))
        cases = prosecution_obj.search(
            self.cr, self.uid, domain)
        return prosecution_obj.browse(self.cr, self.uid, cases)
