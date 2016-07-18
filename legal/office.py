# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_office(models.Model):

    """"""

    _name = 'legal.office'
    _rec_name = 'display_name'

    name = fields.Char(string='Name')
    display_name = fields.Char(compute='_get_display_name', store=True)
    mail = fields.Char(string='Mail')
    location = fields.Char(string='Location', required=True)
    address = fields.Char(string='Address')

    @api.one
    @api.depends('name', 'location')
    def _get_display_name(self):
        self.display_name = self.name or '' + ' - ' + self.location or ''
