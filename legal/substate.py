# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_substate(models.Model):

    """"""

    _name = 'legal.substate'

    name = fields.Char(string='Name')
