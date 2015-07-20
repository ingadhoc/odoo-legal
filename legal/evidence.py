# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_evidence(models.Model):

    """"""

    _name = 'legal.evidence'

    observations = fields.Char(string='Observations')
    offerer_id = fields.Many2one('legal.offerer', string='Offerer')
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')], string='State', default='pending')
    type_id = fields.Many2one('legal.evidence.type', string='Type')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')

    @api.one
    def action_done(self):
        if self.state == 'pending':
            self.state = 'produced'
        elif self.state == 'produced':
            self.state = 'pending'


class legal_evidence_type(models.Model):

    """"""

    _name = 'legal.evidence.type'

    name = fields.Char(String="Name")
