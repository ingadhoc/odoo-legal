# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_events(models.Model):

    """"""

    _name = 'legal.events'

    description = fields.Char(string='Description')
    date = fields.Datetime(string='Date')
    event_type = fields.Char(string='Event type')
    procese_id = fields.Many2one('legal.procese', string='Procese')
