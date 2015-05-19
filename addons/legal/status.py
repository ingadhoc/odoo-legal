# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_status(models.Model):

    """"""

    _name = 'legal.status'

    name = fields.Char(string='Name')
