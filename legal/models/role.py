# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalRole(models.Model):

    _name = 'legal.role'

    name = fields.Char(string='Name')
