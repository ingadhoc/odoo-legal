# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api


class LegalEvidence(models.Model):

    _name = 'legal.evidence'

    observations = fields.Char(
        string='Observations')
    offerer_id = fields.Many2one(
        'legal.offerer',
        string='Offerer')
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')],
        string='State',
        default='pending')
    type_id = fields.Many2one(
        'legal.evidence.type',
        string='Type')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')

    @api.multi
    def action_done(self):
        for rec in self:
            if rec.state == 'pending':
                rec.state = 'produced'
            elif rec.state == 'produced':
                rec.state = 'pending'


class LegalEvidenceType(models.Model):

    _name = 'legal.evidence.type'

    name = fields.Char(String="Name")
