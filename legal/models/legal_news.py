##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields
from datetime import date


class LegalNews(models.Model):

    _name = 'legal.news'
    _rec_name = 'description'

    description = fields.Char()

    date = fields.Date(
        default=date.today(),
    )

    type_id = fields.Many2one(
        'legal.news.type',
    )

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )

