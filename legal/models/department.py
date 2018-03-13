# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalDepartment(models.Model):

    _name = 'legal.department'

    name = fields.Char('Name')
    code = fields.Char('Code', required=True)
