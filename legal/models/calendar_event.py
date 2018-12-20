##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    event_type = fields.Selection(
        [('personal', 'Personal'),
         ('audience', 'Audience'),
         ('expiry', 'Expiry')],
        default='personal',
    )
    prosecution_id = fields.Many2one(
        'legal.prosecution',
    )
    sub_type_id = fields.Many2one(
        'legal.meeting.type',
        string='Metting Subtype',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        related='prosecution_id.partner_id',
    )
    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer',
        related='prosecution_id.responsible_id',
    )
    prosecution_type_id = fields.Many2one(
        'legal.prosecution_type',
        string='Type of prosecution',
        related='prosecution_id.prosecution_type_id',
    )
    department_id = fields.Many2one(
        string='Department',
        related='prosecution_id.department_id',
    )
    caratula = fields.Char(
        related='prosecution_id.caratula',
    )
    number_case_file = fields.Char(
        string='Number of case file',
        related='prosecution_id.number_case_file',
    )
    current_judged_id = fields.Many2one(
        'legal.office',
        related='prosecution_id.current_judged_id',
    )

    @api.multi
    @api.constrains('prosecution_id')
    def update_attendee(self):
        for rec in self:
            if rec.prosecution_id.member_ids:
                rec.partner_ids = [
                    x.partner_id.id for x in rec.prosecution_id.member_id
                ]

    @api.onchange('event_type')
    def update_event_type(self):
        if self.event_type:
            self.sub_type_id = False
