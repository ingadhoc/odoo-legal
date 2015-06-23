# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_event(models.Model):

    """"""

    _name = 'legal.event'
    _rec_name = 'description'

    description = fields.Char(string='Description')
    date = fields.Datetime(string='Date')
    type_id = fields.Many2one('legal.event.type', string='Type')
    process_id = fields.Many2one('legal.process', string='process')


class legal_event_type(models.Model):

    """"""

    _name = 'legal.event.type'

    name = fields.Char(String="Name")
