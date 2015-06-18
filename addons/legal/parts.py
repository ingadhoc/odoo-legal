# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_parts(models.Model):

    """"""

    _name = 'legal.parts'

    age = fields.Integer(string='Age')
    contact_id = fields.Many2one(
        'res.partner', string='Contact', domain="[('customer','=',True)]")
    role = fields.Many2one('legal.role', string='Role')
    lawyer_id = fields.Many2one(
        'res.users', string='Lawyer', domain="[('is_lawyer','=',True)]")
    procese_id = fields.Many2one('legal.procese', string='Procese')
