# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_audiences(models.Model):

    """"""

    _name = 'legal.audiences'

    type_id = fields.Many2one('legal.audiences.type', string='Type')
    observations = fields.Char(string='Observations')
    date = fields.Datetime(string='Date')
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')], string='State', default='pending')
    prosecution_id = fields.Many2one('legal.prosecution', string='Prosecution')

    @api.one
    def action_done(self):
        if self.state == 'pending':
            self.state = 'produced'
        elif self.state == 'produced':
            self.state = 'pending'


class legal_audiences_type(models.Model):

    """"""

    _name = 'legal.audiences.type'

    name = fields.Char(string='Name')
