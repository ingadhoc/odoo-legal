# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_formed(models.Model):

    """"""

    _name = 'legal.formed'

    name = fields.Char(string='Name')
