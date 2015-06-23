# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_role(models.Model):

    """"""

    _name = 'legal.role'

    name = fields.Char(string='Name')
