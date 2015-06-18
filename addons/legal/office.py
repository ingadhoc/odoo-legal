# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_office(models.Model):

    """"""

    _name = 'legal.office'

    name = fields.Char(string='Name')
    mail = fields.Char(string='Mail')
    location = fields.Char(string='Location', required=True)
    address = fields.Char(string='Address')
