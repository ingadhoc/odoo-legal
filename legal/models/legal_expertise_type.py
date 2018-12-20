##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalExpertiseType(models.Model):

    _name = 'legal.expertise.type'

    name = fields.Char()
