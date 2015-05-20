# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_office(models.Model):

    """"""

    _name = 'legal.office'

    name = fields.Char(string='Name')
    mail = fields.Char(string='Mail')
