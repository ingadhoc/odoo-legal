##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class LegalEvidence(models.Model):

    _name = 'legal.evidence'

    observations = fields.Char()

    offerer_id = fields.Many2one(
        'legal.offerer',
    )
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')],
        default='pending',
    )
    type_id = fields.Many2one(
        'legal.evidence.type',
    )
    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )

    @api.multi
    def action_done(self):
        for rec in self:
            if rec.state == 'pending':
                rec.state = 'produced'
            elif rec.state == 'produced':
                rec.state = 'pending'
