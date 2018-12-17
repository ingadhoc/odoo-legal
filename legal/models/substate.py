# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalSubstate(models.Model):

    _name = 'legal.substate'

    name = fields.Char(string='Name')
