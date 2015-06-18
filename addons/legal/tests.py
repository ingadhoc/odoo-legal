# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_tests(models.Model):

    """"""

    _name = 'legal.tests'

    description = fields.Char(string='Description')
    event_id = fields.Many2one('legal.events', string='Event')
    procese_id = fields.Many2one('legal.procese', string='Procese')
