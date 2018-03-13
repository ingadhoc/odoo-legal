# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class Partner(models.Model):

    _inherit = 'res.partner'

    is_lawyer = fields.Boolean(string='Is lawyer?')
