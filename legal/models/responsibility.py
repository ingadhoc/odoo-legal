# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalResponsibility(models.Model):

    _name = 'legal.responsibility'

    name = fields.Char(string='Name')
