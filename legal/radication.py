# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_radication(models.Model):

    """"""

    _name = 'legal.radication'
    _order = 'date desc'

    address = fields.Char(string='Address', compute='_get_address')
    judged_id = fields.Many2one('legal.office', string='Judged')
    num_1_ins = fields.Char(string='Num. 1°Ins')
    num_2_ins = fields.Char(string='Num. 2°Ins')
    num_3_ins = fields.Char(string='Num. 3°Ins')
    num_filed = fields.Char(string='Num. Filed')
    date = fields.Date(string='Date')
    process_id = fields.Many2one('legal.process', string='process')

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
