# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_department(models.Model):

    _name = 'legal.department'

    name = fields.Char('Name')
    code = fields.Char('Code', required=True)
