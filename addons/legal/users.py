# -*- coding: utf-8 -*-
from openerp import models, fields


class user(models.Model):

    """"""

    _inherit = 'res.users'

    is_lawyer = fields.Boolean(string='Is lawyer?')
