# -*- coding: utf-8 -*-
from openerp import models, fields


class partner(models.Model):

    """"""

    _inherit = 'res.partner'

    is_lawyer = fields.Boolean(string='Is lawyer?')
