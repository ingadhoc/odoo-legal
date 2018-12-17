# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class LegalPart(models.Model):

    _name = 'legal.part'

    age = fields.Integer(string='Age')
    contact = fields.Char(string='Contact')
    dni = fields.Integer(string='DNI')
    role_id = fields.Many2one('legal.role',
                              string='Role')
    lawyer_id = fields.Many2one(
        'res.partner',
        string='Lawyer',
        domain="[('is_lawyer','=',True)]",
        context={'default_is_lawyer': True})
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')
