# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from datetime import date


class prosecution(models.Model):

    """"""

    _name = 'legal.prosecution'
    _description = 'prosecution'
    _inherit = ['mail.thread']
    _rec_name = 'folder_name'

    @api.one
    def action_compute(self):
        self.folder_name = '-'.join([str(self.department_id.code), self.partner_id.name[0],
                                     self.env['ir.sequence'].get('legal.prosecution')])

    def create(self, cr, uid, vals, context=None):
        name = ''
        partner_obj = self.pool['res.partner']
        department_obj = self.pool['legal.department']
        if vals.get('department_id', False):
            name = str(department_obj.browse(
                cr, uid,
                vals.get('department_id', False), context=context).code)
        if vals.get('partner_id', False):
            name += '-' + partner_obj.browse(
                cr, uid, vals.get('partner_id', False), context=context).name[0]
        name += '-' + \
            self.pool['ir.sequence'].get(cr, uid, 'legal.prosecution')
        vals['folder_name'] = name
        vals['opening_date_folder'] = date.today()
        return super(prosecution, self).create(cr, uid, vals, context=None)

    @api.one
    @api.depends('radication_ids')
    def _get_data(self):
        if self.radication_ids:
            self.current_judged_id = self.radication_ids[
                0].judged_id.id
            self.number_case_file = self.radication_ids[0].num_case_file

        else:
            self.current_judged_id = []
            self.number_case_file = ''

    @api.one
    def _audiences_event_count(self):
        self.audiences_event_count = len(
            self.sudo().event_audiences_ids.filtered(
                lambda x: x.state == 'draft'))

    @api.one
    def _expiry_event_count(self):
        self.expiry_event_count = len(
            self.sudo().event_expiry_ids.filtered(
                lambda x: x.state == 'draft'))

    @api.one
    def _calculate_amount(self):
        self.claim_amount = sum([x.total for x in self.claim_ids])

    @api.one
    @api.constrains('member_ids')
    def action_follow(self):
        return self.message_subscribe_users(self.member_ids.ids)

    @api.one
    @api.onchange('prosecution_type_id')
    def auto_complete_auxiliar_field(self):
        self.auxiliary_ids = self.env[
            'legal.auxiliary']
        auxiliary_field_obj = self.env['legal.auxiliary.field']
        if self.prosecution_type_id:
            auxiliary_field_ids = auxiliary_field_obj.search(
                [('prosecution_type_id', '=', self.prosecution_type_id.id)])
            lines = []
            for line in auxiliary_field_ids:
                values = {
                    'field_id': line.id,
                }
                lines.append((0, _, values))
            self.auxiliary_ids = lines

    audiences_event_count = fields.Integer(compute='_audiences_event_count')
    expiry_event_count = fields.Integer(compute='_expiry_event_count')
    claim_amount = fields.Float(
        compute='_calculate_amount', string='Claim amount')
    caratula = fields.Char(string='Caratula', required=True)
    color = fields.Integer('Color Index')
    sequence = fields.Char('Sequence')
    member_ids = fields.Many2many(
        'res.users',
        'prosecution_user_rel',
        'prosecution_id', 'uid', 'Prosecution Members')
    prosecution_type_id = fields.Many2one(
        'legal.prosecution_type',
        string='Type of prosecution')
    folder_name = fields.Char(
        string='Folder Name', readonly=True)
    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer', domain="[('is_lawyer','=',True)]",
        context={'default_is_lawyer': True})
    responsibility_id = fields.Many2one(
        'legal.responsibility', string='Responsibility')
    general_state = fields.Selection(
        [('open', 'Open'),
         ('closed', 'Closed')],
        'General State', default='open', track_visibility='onchange')
    status_id = fields.Many2one('legal.status', string='Status')
    opening_date_folder = fields.Date(string="Opening date Folder")
    re_opening_date_folder = fields.Date(string="Re-Opening date Folder")
    close_date_folder = fields.Date(string="Close date folder")
    demand_start_date = fields.Date(string="Demand start date")
    radication_ids = fields.One2many(
        'legal.radication', 'prosecution_id', string='Radication')
    claim_ids = fields.One2many(
        'legal.claim', 'prosecution_id', string='Claims')
    claim_type_ids = fields.Many2many(
        'legal.claim.type',
        'legal_type_claim_ids_prosecution_id_rel',
        'prosecution_id',
        'name', string='Type of Claims')
    auxiliary_ids = fields.One2many(
        'legal.auxiliary', 'prosecution_id', string='Auxiliary Fields')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_prosecution_ids_rel',
        'prosecution_id',
        'attachment_id', string='Attachments')
    regulation_ids = fields.One2many(
        'legal.regulation', 'prosecution_id', string='Regulation')
    substate_id = fields.Many2one('legal.substate', string="Substate")
    current_judged_id = fields.Many2one(
        'legal.office',
        string='Current Judged', compute='_get_data', store=True)
    news_ids = fields.One2many(
        'legal.news',
        'prosecution_id', string="News")
    partner_id = fields.Many2one(
        'res.partner', 'Customer', domain="[('customer','=',True)]")
    num_sinister = fields.Char(string="Number of sinister")
    number_case_file = fields.Char(
        'Number of case file',
        compute='_get_data', store=True)
    part_ids = fields.One2many('legal.part', 'prosecution_id', string='Parts')
    note = fields.Text('Notes')
    negotiation_ids = fields.One2many(
        'legal.negotiation', 'prosecution_id', string="Negotiation")
    evidence_ids = fields.One2many(
        'legal.evidence', 'prosecution_id', string="Evidence")
    event_audiences_ids = fields.One2many(
        'calendar.event',
        'prosecution_id',
        string="Audiences",
        domain=[('event_type', '=', 'audience')],
        context={'default_event_type': 'audience'})
    event_expiry_ids = fields.One2many(
        'calendar.event',
        'prosecution_id',
        string="Expiry",
        domain=[('event_type', '=', 'expiry')],
        context={'default_event_type': 'expiry'})
    expertise_ids = fields.One2many(
        'legal.expertise', 'prosecution_id', string="Expertise")
    description_of_claim = fields.Html(string='Description of claim')
    department_id = fields.Many2one('legal.department', string='Department')
    invoice_ids = fields.One2many(
        'account.invoice', 'prosecution_id', string='invoices')
    invoices = fields.Integer(compute='_get_number_of_invoices')
    state_detail_id = fields.Many2one(
        'prosecution.state_detail',
        string='State Detail',
        track_visibility='onchange',
        select=True
    )

    @api.one
    def set_open(self):
        self.general_state = 'open'
        self.re_opening_date_folder = date.today()

    @api.one
    def set_close(self):
        self.general_state = 'closed'
        self.close_date_folder = date.today()
        self.re_opening_date_folder = False

    @api.one
    def _get_number_of_invoices(self):
        if self.invoice_ids:
            self.invoices = len(self.invoice_ids)

    @api.constrains('general_state')
    def onchange_general_state(self):
        if self.general_state:
            state_detail = self.env['prosecution.state_detail'].search(
                [('state', '=', self.general_state)], limit=1)
            self.state_detail_id = state_detail.id


class legal_type_prosecution(models.Model):

    """"""

    _name = 'legal.prosecution_type'
    _description = 'type prosecution'

    name = fields.Char('Name')
    code = fields.Integer('Code')


class prosecution_state_detail(models.Model):
    _name = 'prosecution.state_detail'
    _order = 'sequence'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')
    state = fields.Selection(
        store=True,
        selection=[('open', 'Open'),
                   ('closed', 'Closed')], string='Status'
    )
    prosecution_ids = fields.One2many(
        'legal.prosecution',
        'state_detail_id',
        'Prosecutions')
