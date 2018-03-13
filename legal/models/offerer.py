# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalOfferer(models.Model):

    _name = 'legal.offerer'

    name = fields.Char(string='Name')
