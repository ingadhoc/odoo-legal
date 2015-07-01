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
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')
    customer_id = fields.Many2one('res.partner', compute='get_contact')

    @api.one
    @api.depends('prosecution_id', 'prosecution_id.part_ids')
    def get_contact(self):
        self.part_contact_ids = self.prosecution_id.part_ids.mapped(
            'contact_id')
        self.customer_id = self.prosecution_id.partner_id.id
