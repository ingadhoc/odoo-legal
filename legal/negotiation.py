# -*- coding: utf-8 -*-
from openerp import models, fields
from datetime import date


class legal_negotiation(models.Model):

    """"""

    _name = 'legal.negotiation'

    concept_id = fields.Many2one('legal.negotiation.concept', string='Concept')
    date_proposal = fields.Date(
        string='Date Proposal', default=date.today())
    amount = fields.Float(string='Amount')
    observations = fields.Char(string='Observations')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')


class legal_negotiation_concept(models.Model):

    """"""

    _name = 'legal.negotiation.concept'

    name = fields.Char(string='Name')
