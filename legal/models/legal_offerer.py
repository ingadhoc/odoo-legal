##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalOfferer(models.Model):

    _name = 'legal.offerer'

    name = fields.Char()
