##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields

class ProsecutionStateDetail(models.Model):
    _name = 'prosecution.state_detail'
    _order = 'sequence'

    name = fields.Char()

    sequence = fields.Integer()

    state = fields.Selection(
        store=True,
        selection=[
            ('open', 'Open'),
            ('closed', 'Closed')],
        string='Status',
    )

    prosecution_ids = fields.One2many(
        'legal.prosecution',
        'state_detail_id',
        'Prosecutions',
    )
