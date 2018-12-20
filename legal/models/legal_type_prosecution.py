##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields

class LegalTypeProsecution(models.Model):

    _name = 'legal.prosecution_type'
    _description = 'type prosecution'

    name = fields.Char()
    code = fields.Integer()
