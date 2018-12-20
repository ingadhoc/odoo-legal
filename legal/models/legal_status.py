##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalStatus(models.Model):

    _name = 'legal.status'

    name = fields.Char()
