# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api


class LegalOffice(models.Model):

    _name = 'legal.office'
    _rec_name = 'display_name'

    name = fields.Char(
        string='Name')
    display_name = fields.Char(
        compute='_compute_display_name',
        store=True)
    mail = fields.Char(string='Mail')
    location = fields.Char(
        string='Location',
        required=True)
    address = fields.Char(string='Address')

    @api.multi
    @api.depends('name', 'location')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = ' - '.join([rec.name or ' ',
                                           rec.location or ' '])
