# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo.report.report_sxw import rml_parse
import logging
logger = logging.getLogger('report_aeroo')


class Parser(rml_parse):

    def __init__(self, cr, uid, name, context):
        super(self.__class__, self).__init__(cr, uid, name, context)

        if not context:
            return None

        self.from_date = context.get('from_date', False)
        self.to_date = context.get('to_date', False)
        self.detail = context.get('detail', False)
        self.responsible_id = context.get('responsible_id', False)
        self.prosecution_type_id = context.get('prosecution_type_id', False)

        self.localcontext.update({
            'context': context,
            'show_cases_initial': self.show_cases_initial,
            'show_cases_new': self.show_cases_new,
            'show_cases_close': self.show_cases_close,
            'show_cases_re_open': self.show_cases_re_open,
        })

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
