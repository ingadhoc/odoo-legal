# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################

from openerp import models, fields


class LegalModel(models.Model):

    _name = 'legal.model'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    type = fields.Selection(
        [('writing', 'Writing'),
         ('listing', 'Listing'),
         ('glossaries', 'Glossaries')],
        string='Type')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_legal_models_ids_rel',
        'legal_models_id',
        'attachment_id',
        string='Attachments')
