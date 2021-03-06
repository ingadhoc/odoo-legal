##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalDepartment(models.Model):

    _name = 'legal.department'

    name = fields.Char('Name')
    code = fields.Char('Code', required=True)
