# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_offerer(models.Model):

    """"""

    _name = 'legal.offerer'

    name = fields.Char(string='Name')
