##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields
from datetime import date


class LegalNews(models.Model):

    _name = 'legal.news'
    _rec_name = 'description'

    description = fields.Char(string='Description')
    date = fields.Date(
        string='Date',
        default=date.today())
    type_id = fields.Many2one(
        'legal.news.type',
        string='Type')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')


class LegalNewsType(models.Model):

    _name = 'legal.news.type'

    name = fields.Char(String="Name")
