# -*- coding: utf-8 -*-
from openerp import models, fields
from datetime import date


class legal_regulation(models.Model):

    """"""

    _name = 'legal.regulation'

    beneficiary = fields.Char(string='Beneficiary')
    concept_id = fields.Many2one('legal.regulation.concept', string='Concept')
    date_order = fields.Date(string="Date of the order", default=date.today())
    date_maturity = fields.Date(string="Date of the maturity")
    date_fulfillment = fields.Date(string="Date of the fulfillment")
    amount = fields.Float(string="Amount", store=True)
    observations = fields.Char(string='Observations')
    check_num = fields.Integer(string='Check Number')
    prosecution_id = fields.Many2one('legal.prosecution', string='Prosecution')


class legal_regulation_concept(models.Model):

    """"""

    _name = 'legal.regulation.concept'

    name = fields.Char(string='Name')
