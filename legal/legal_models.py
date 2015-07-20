# -*- coding: utf-8 -*-


from openerp import models, fields


class legal_model(models.Model):

    """"""

    _name = 'legal.model'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    type = fields.Selection(
        [('writing', 'Writing'),
         ('listing', 'Listing'), ('glossaries', 'Glossaries')],
        string='Type')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_legal_models_ids_rel',
        'legal_models_id',
        'attachment_id', string='Attachments')
