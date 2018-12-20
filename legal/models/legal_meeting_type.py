##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class LegalMeetingType(models.Model):

    _name = 'legal.meeting.type'

    name = fields.Char(string='Name')
    event_type = fields.Selection(
        [('personal', 'Personal'),
         ('audience', 'Audience'),
         ('expiry', 'Expiry')],
        required=True,
    )
