# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_negotiation(models.Model):

    """"""

    _name = 'legal.negotiation'

    part_contact_ids = fields.Many2many(
        'res.partner', compute='get_contact', string='Contacts')
    who_id = fields.Many2one('res.partner', string='Who')
    payer_id = fields.Many2one('res.partner', string='Payer')
    beneficiary_id = fields.Many2one('res.partner', string='Beneficiary')
    date_proposal = fields.Datetime(string='Date Proposal')
    amount = fields.Float(string='Amount')
    observations = fields.Char(string='Observations')
    procese_id = fields.Many2one('legal.procese', string='Procese')

    @api.one
    @api.depends('procese_id', 'procese_id.part_ids')
    def get_contact(self):
        self.part_contact_ids = self.procese_id.part_ids.mapped('contact_id')
