##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields


class LegalModel(models.Model):

    _name = 'legal.model'

    name = fields.Char()

    description = fields.Char()

    type = fields.Selection([
        ('writing', 'Writing'),
        ('listing', 'Listing'),
        ('glossaries', 'Glossaries')
        ],
    )
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_legal_models_ids_rel',
        'legal_models_id',
        'attachment_id',
    )
