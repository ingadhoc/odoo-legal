##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalNewsType(models.Model):

    _name = 'legal.news.type'

    name = fields.Char()

