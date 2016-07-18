# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_radication(models.Model):

    """"""

    _name = 'legal.radication'
    _order = 'date_court desc'

    address = fields.Char(string='Address', compute='_get_address')
    judged_id = fields.Many2one('legal.office', string='Judged')
    num_case_file = fields.Char(string='Num. case file')
    date_court = fields.Date(string='Date of admission to court')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')

    @api.one
    @api.depends(
        'judged_id', 'judged_id.location')
    def _get_address(self):
        address = ''
        if self.judged_id:
            address = self.judged_id.location
            if self.judged_id.address:
                address += '-' + self.judged_id.address
        self.address = address
