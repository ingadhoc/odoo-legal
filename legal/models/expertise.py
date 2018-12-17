##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _


class LegalExpertise(models.Model):

    _name = 'legal.expertise'

    type_id = fields.Many2one(
        'legal.expertise.type',
        string='Type')
    offerer_id = fields.Many2one(
        'legal.offerer',
        string='Offerer')
    name = fields.Char(
        string='Name')
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')],
        string='State',
        default='pending')
    observations = fields.Char(
        string='Observations')
    prosecution_id = fields.Many2one(
        'legal.prosecution',
        string='prosecution')
    expertise_detail_ids = fields.One2many(
        'legal.expertise.detail',
        'expertise_id',
        string='Expertise Detail')
    expertise_detail = fields.Text(
        string='Expertise Detail',
        compute='_compute_expertise_detail')

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


class LegalExpertiseType(models.Model):

    _name = 'legal.expertise.type'

    name = fields.Char(string='Name')


class LegalExpertiseDetail(models.Model):

    _name = 'legal.expertise.detail'

    detail_type_id = fields.Many2one(
        'legal.expertise.detail_type',
        string='Detail Type')
    value = fields.Char(
        string='Value')
    expertise_id = fields.Many2one(
        'legal.expertise',
        string='Expertise')


class LegalExpertiseDetailType(models.Model):

    _name = 'legal.expertise.detail_type'

    name = fields.Char(string='Name')
    expertise_type_id = fields.Many2one(
        'legal.expertise.type',
        string='Expertise Type')
