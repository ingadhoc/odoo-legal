# -*- coding: utf-8 -*-


from openerp import models, fields


class legal_models(models.Model):

    """"""

    _name = 'legal.models'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    types = fields.Selection(
        [('writings', 'Writings'),
         ('listings', 'Listings'), ('glossaries', 'Glossaries')],
        string='Type')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_legal_models_ids_rel',
        'legal_models_id',
        'attachment_id', string='Attachments')
