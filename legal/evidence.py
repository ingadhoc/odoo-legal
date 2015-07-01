# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_evidence(models.Model):

    """"""

    _name = 'legal.evidence'

    description = fields.Char(string='Description')
    event_id = fields.Many2one('legal.event', string='Event')
    date = fields.Datetime(string='Date')
    type_id = fields.Many2one('legal.evidence.type', string='Type')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')


class legal_evidence_type(models.Model):

    """"""

    _name = 'legal.evidence.type'

    name = fields.Char(String="Name")
