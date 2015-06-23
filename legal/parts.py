# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_part(models.Model):

    """"""

    _name = 'legal.part'

    age = fields.Integer(string='Age')
    contact_id = fields.Many2one(
        'res.partner', string='Contact')
    role_id = fields.Many2one('legal.role', string='Role')
    lawyer_id = fields.Many2one(
        'res.partner', string='Lawyer', domain="[('is_lawyer','=',True)]")
    process_id = fields.Many2one('legal.process', string='process')
