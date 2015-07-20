# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_responsibility(models.Model):

    """"""

    _name = 'legal.responsibility'

    name = fields.Char(string='Name')
