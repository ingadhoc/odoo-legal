# -*- coding: utf-8 -*-
from openerp import models, fields, api


class calendar_event(models.Model):

    _inherit = 'calendar.event'

    event_type = fields.Selection(
        [('personal', 'Personal'),
         ('audience', 'Audience'),
         ('expiry', 'Expiry')], string='Event Type', default='personal')
    prosecution_id = fields.Many2one(
        'legal.prosecution', string='Prosecution')
    sub_type_id = fields.Many2one(
        'legal.meeting.type',
        string='Metting Subtype')
    partner_id = fields.Many2one(
        'res.partner', 'Customer', related='prosecution_id.partner_id')
    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer', related='prosecution_id.responsible_id')
    prosecution_type_id = fields.Many2one(
        'legal.prosecution_type',
        string='Type of prosecution',
        related='prosecution_id.prosecution_type_id')

    @api.one
    @api.constrains('prosecution_id')
    def update_attendee(self):
        if self.prosecution_id.member_ids:
            self.partner_ids = [
                x.partner_id.id for x in self.prosecution_id.member_ids]

    @api.onchange('event_type')
    def update_event_type(self):
        if self.event_type:
            self.sub_type_id = False


class legal_meeting_type(models.Model):

    """"""

    _name = 'legal.meeting.type'

    name = fields.Char(string='Name')
    event_type = fields.Selection(
        [('personal', 'Personal'),
         ('audience', 'Audience'),
         ('expiry', 'Expiry')], string='Event Type', required=True)
