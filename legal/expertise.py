# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class legal_expertise(models.Model):

    """"""

    _name = 'legal.expertise'

    type_id = fields.Many2one('legal.expertise.type', string='Type')
    offerer_id = fields.Many2one('legal.offerer', string='Offerer')
    name = fields.Char(string='Name')
    state = fields.Selection(
        [('pending', 'Pending'),
         ('produced', 'Produced')], string='State', default='pending')
    observations = fields.Char(string='Observations')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')
    expertise_detail_ids = fields.One2many(
        'legal.expertise.detail', 'expertise_id', string='Expertise Detail')
    expertise_detail = fields.Text(
        string='Expertise Detail', compute='_get_expertise_detail')

    @api.one
    def _get_expertise_detail(self):
        if self.expertise_detail_ids:
            expertise_detail = ''
            for expertise_detail_item in self.expertise_detail_ids:
                expertise_detail = expertise_detail + \
                    ' : '.join([expertise_detail_item.detail_type_id.name or ' ',
                                expertise_detail_item.value or ' ']) + '\n'
            self.expertise_detail = expertise_detail

    @api.one
    def action_done(self):
        if self.state == 'pending':
            self.state = 'produced'
        elif self.state == 'produced':
            self.state = 'pending'

    @api.one
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


class legal_expertise_type(models.Model):

    """"""

    _name = 'legal.expertise.type'

    name = fields.Char(string='Name')


class legal_expertise_detail(models.Model):

    """"""

    _name = 'legal.expertise.detail'

    detail_type_id = fields.Many2one(
        'legal.expertise.detail_type', string='Detail Type')
    value = fields.Char(string='Value')
    expertise_id = fields.Many2one('legal.expertise', string='Expertise')


class legal_expertise_detail_type(models.Model):

    """"""

    _name = 'legal.expertise.detail_type'

    name = fields.Char(string='Name')
    expertise_type_id = fields.Many2one(
        'legal.expertise.type', string='Expertise Type')
