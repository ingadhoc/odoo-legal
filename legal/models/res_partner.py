##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class Partner(models.Model):

    _inherit = 'res.partner'

    is_lawyer = fields.Boolean(string='Is lawyer?')
