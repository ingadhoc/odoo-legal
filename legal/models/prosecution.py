##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields, api, _
from datetime import date


class Prosecution(models.Model):

    _name = 'legal.prosecution'
    _description = 'prosecution'
    _inherit = ['mail.thread']
    _rec_name = 'folder_name'

    @api.multi
    def action_compute(self):
        for rec in self:
            rec.folder_name = '-'.join(
                [str(rec.department_id.code), rec.partner_id.name[0],
                 self.env['ir.sequence'].get('legal.prosecution')]
            )

    @api.model
    def create(self, vals):
        name = ''
        partner_obj = self.env['res.partner']
        department_obj = self.env['legal.department']
        if vals.get('department_id', False):
            name = str(department_obj.browse(
                vals.get('department_id', False)).code)
        if vals.get('partner_id', False):
            name += '-' + partner_obj.browse(
                vals.get('partner_id', False)).name[0]
        name += '-' + \
            self.env['ir.sequence'].get('legal.prosecution')
        vals['folder_name'] = name
        vals['opening_date_folder'] = date.today()
        return super(Prosecution, self).create(vals)

    @api.multi
    @api.depends('radication_ids')
    def _get_data(self):
        for rec in self:
            if rec.radication_ids:
                rec.current_judged_id = rec.radication_ids[
                    0].judged_id.id
                rec.number_case_file = rec.radication_ids[0].num_case_file
            else:
                rec.current_judged_id = []
                rec.number_case_file = ''

    @api.multi
    def _compute_audiences_event_count(self):
        for rec in self:
            rec.audiences_event_count = len(
                rec.sudo().event_audiences_ids.filtered(
                    lambda x: x.state == 'draft'))

    @api.multi
    def _compute_expiry_event_count(self):
        for rec in self:
            rec.expiry_event_count = len(
                rec.sudo().event_expiry_ids.filtered(
                    lambda x: x.state == 'draft'))

    @api.multi
    def _compute_claim_amount(self):
        for rec in self:
            rec.claim_amount = sum(rec.claim_ids.mapped('total'))

    @api.multi
    @api.constrains('member_ids')
    def action_follow(self):
        for rec in self:
            rec.message_subscribe_users(self.member_ids.ids)

    @api.multi
    @api.onchange('department_id')
    def auto_complete_auxiliar_field(self):
        for rec in self:
            rec.auxiliary_ids = self.env[
                'legal.auxiliary']
            if rec.department_id:
                auxiliary_field_ids = self.env['legal.auxiliary.field'].search(
                    [('department_id', '=', rec.department_id.id)])
                lines = []
                for line in auxiliary_field_ids:
                    values = {
                        'field_id': line.id,
                    }
                    lines.append((0, _, values))
                rec.auxiliary_ids = lines

    @api.multi
    def update_auxiliar_field(self):
        for rec in self:
            if rec.department_id:
                auxiliary_field_ids = self.env['legal.auxiliary.field'].search(
                    [('department_id', '=', rec.department_id.id),
                     ('id', 'not in', rec.auxiliary_ids
                        .mapped('field_id').ids)])
                lines = []
                for line in auxiliary_field_ids:
                    values = {
                        'field_id': line.id,
                    }
                    lines.append((0, _, values))
                rec.auxiliary_ids = lines

    audiences_event_count = fields.Integer(
        compute='_compute_audiences_event_count',
    )

    expiry_event_count = fields.Integer(
        compute='_compute_expiry_event_count',
    )
    claim_amount = fields.Float(
        compute='_compute_claim_amount',
        string='Claim amount',
    )

    caratula = fields.Char(
        string='Caratula',
        required=True,
    )

    color = fields.Integer('Color Index')

    sequence = fields.Char('Sequence')

    member_ids = fields.Many2many(
        'res.users',
        'prosecution_user_rel',
        'prosecution_id',
        'uid',
        'Prosecution Members',
    )

    prosecution_type_id = fields.Many2one(
        'legal.prosecution_type',
        string='Type of prosecution',
    )

    folder_name = fields.Char(
        string='Folder Name',
        readonly=True,
    )

    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer',
        domain="[('is_lawyer','=',True)]",
        context={'default_is_lawyer': True},
    )

    responsibility_id = fields.Many2one(
        'legal.responsibility',
        string='Responsibility',
    )

    general_state = fields.Selection(
        [('open', 'Open'),
         ('closed', 'Closed')],
        'General State',
        default='open',
        track_visibility='onchange',
    )

    status_id = fields.Many2one(
        'legal.status',
        string='Status',
    )

    opening_date_folder = fields.Date(string="Opening date Folder")

    re_opening_date_folder = fields.Date(string="Re-Opening date Folder")

    close_date_folder = fields.Date(string="Close date folder")

    demand_start_date = fields.Date(string="Demand start date")

    sinister_date = fields.Date(string="Sinister Date")

    radication_ids = fields.One2many(
        'legal.radication',
        'prosecution_id',
        string='Radication',
    )

    claim_ids = fields.One2many(
        'legal.claim',
        'prosecution_id',
        string='Claims',
    )

    claim_type_ids = fields.Many2many(
        'legal.claim.type',
        'legal_type_claim_ids_prosecution_id_rel',
        'prosecution_id',
        'name',
        string='Type of Claims',
    )

    auxiliary_ids = fields.One2many(
        'legal.auxiliary',
        'prosecution_id',
        string='Auxiliary Fields',
    )

    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_prosecution_ids_rel',
        'prosecution_id',
        'attachment_id',
        string='Attachments',
    )

    regulation_ids = fields.One2many(
        'legal.regulation',
        'prosecution_id',
        string='Regulation',
    )

    substate_id = fields.Many2one(
        'legal.substate',
        string="Substate",
    )

    current_judged_id = fields.Many2one(
        'legal.office',
        string='Current Judged',
        compute='_get_data',
        store=True,
    )

    news_ids = fields.One2many(
        'legal.news',
        'prosecution_id',
        string="News",
    )

    partner_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain="[('customer','=',True)]",
    )

    num_sinister = fields.Char(
        string="Number of sinister",
    )

    number_case_file = fields.Char(
        'Number of case file',
        compute='_get_data',
        store=True,
    )

    part_ids = fields.One2many(
        'legal.part',
        'prosecution_id',
        string='Parts',
    )

    note = fields.Text('Notes')

    negotiation_ids = fields.One2many(
        'legal.negotiation',
        'prosecution_id',
        string="Negotiation",
    )

    evidence_ids = fields.One2many(
        'legal.evidence',
        'prosecution_id',
        string="Evidence",
    )

    event_audiences_ids = fields.One2many(
        'calendar.event',
        'prosecution_id',
        string="Audiences",
        domain=[('event_type', '=', 'audience')],
        context={'default_event_type': 'audience'},
    )

    event_expiry_ids = fields.One2many(
        'calendar.event',
        'prosecution_id',
        string="Expiry",
        domain=[('event_type', '=', 'expiry')],
        context={'default_event_type': 'expiry'},
    )

    expertise_ids = fields.One2many(
        'legal.expertise',
        'prosecution_id',
        string="Expertise",
    )

    description_of_claim = fields.Html(string='Description of claim')

    department_id = fields.Many2one(
        'legal.department',
        string='Department',
    )

    invoice_ids = fields.One2many(
        'account.invoice',
        'prosecution_id',
        string='invoices',
    )

    invoices = fields.Integer(compute='_compute_invoices')

    state_detail_id = fields.Many2one(
        'prosecution.state_detail',
        string='State Detail',
        track_visibility='onchange',
        index=True,
    )
    scene_sinister = fields.Char(string="Scene of the sinister")

    @api.multi
    def set_open(self):
        for rec in self:
            rec.general_state = 'open'
            rec.re_opening_date_folder = date.today()

    @api.multi
    def set_close(self):
        for rec in self:
            rec.general_state = 'closed'
            rec.close_date_folder = date.today()
            rec.re_opening_date_folder = False

    @api.multi
    def _compute_invoices(self):
        for rec in self:
            if rec.invoice_ids:
                rec.invoices = len(rec.invoice_ids)

    @api.multi
    @api.constrains('general_state')
    def onchange_general_state(self):
        for rec in self:
            if rec.general_state:
                state_detail = self.env['prosecution.state_detail'].search(
                    [('state', '=', rec.general_state)], limit=1)
                rec.state_detail_id = state_detail.id


class ProsecutionStateDetail(models.Model):
    _name = 'prosecution.state_detail'
    _order = 'sequence'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')
    state = fields.Selection(
        store=True,
        selection=[
            ('open', 'Open'),
            ('closed', 'Closed')],
        string='Status'
    )
    prosecution_ids = fields.One2many(
        'legal.prosecution',
        'state_detail_id',
        'Prosecutions')
