##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _


class LegalExpertise(models.Model):

    _name = 'legal.expertise'

    type_id = fields.Many2one(
        'legal.expertise.type',
    )

    offerer_id = fields.Many2one(
        'legal.offerer',
    )

    name = fields.Char()

    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')],
        default='pending',
    )

    observations = fields.Char()

    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )

    expertise_detail_ids = fields.One2many(
        'legal.expertise.detail',
        'expertise_id',
    )

    expertise_detail = fields.Text(
        compute='_compute_expertise_detail',
    )

    @api.multi
    def _compute_expertise_detail(self):
        for rec in self:
            if rec.expertise_detail_ids:
                expertise_detail = ''
                for expertise_detail_item in rec.expertise_detail_ids:
                    expertise_detail = expertise_detail + \
                        ' : '.join(
                            [expertise_detail_item.detail_type_id.name or ' ',
                             expertise_detail_item.value or ' ']) + '\n'
                rec.expertise_detail = expertise_detail

    @api.multi
    def action_done(self):
        for rec in self:
            if rec.state == 'pending':
                rec.state = 'produced'
            elif rec.state == 'produced':
                rec.state = 'pending'

    @api.onchange('type_id')
    def auto_complete_expertise_detail(self):
        self.expertise_detail_ids = self.env[
            'legal.expertise.detail']
        expertise_detail_type_obj = self.env['legal.expertise.detail_type']
        if self.type_id:
            expertise_detail_type_ids = expertise_detail_type_obj.search(
                [('expertise_type_id', '=', self.type_id.id)])
            lines = []
            for line in expertise_detail_type_ids:
                values = {
                    'detail_type_id': line.id,
                }
                lines.append((0, _, values))
            self.expertise_detail_ids = lines
