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
        name = ''
        if self.partner_id:
            name = self.partner_id.name[0]
        if self.prosecution_type_id:
            name += '-' + str(self.prosecution_type_id.code)
        name += '-' + self.env['ir.sequence'].get('legal.prosecution')
        self.folder_name = name

    def create(self, cr, uid, vals, context=None):
        name = ''
        partner_obj = self.pool['res.partner']
        prosecution_type_obj = self.pool['legal.prosecution_type']
        if vals.get('partner_id', False):
            name = partner_obj.browse(
                cr, uid, vals.get('partner_id', False), context=context).name[0]
        if vals.get('prosecution_type_id', False):
            name += '-' + str(prosecution_type_obj.browse(cr, uid,
                                                          vals.get('prosecution_type_id', False), context=context).code)
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
            self.number_current_file = self.radication_ids[0].num_filed
            if not self.radication_ids[0].num_3_ins:
                if not self.radication_ids[0].num_2_ins:
                    if not self.radication_ids[0].num_1_ins:
                        self.last_complete_instance = ''
                    else:
                        self.last_complete_instance = self.radication_ids[
                            0].num_1_ins
                else:
                    self.last_complete_instance = self.radication_ids[
                        0].num_2_ins
            else:
                self.last_complete_instance = self.radication_ids[0].num_3_ins

        else:
            self.last_complete_instance = ''
            self.current_judged_id = []
            self.number_current_file = ''

    @api.one
    def _audiences_count(self):
        """
        Counts the number of audiences the prosecution has, used for smart button
        """
        self.audiences_count = len(self.sudo().audiences_ids)

    audiences_count = fields.Integer(compute='_audiences_count')
    caratula = fields.Char(string='Caratula', required=True)
    color = fields.Integer('Color Index')
    sequence = fields.Char('Sequence')
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
        'legal.news', 'prosecution_id', string="News")
    partner_id = fields.Many2one(
        'res.partner', 'Customer', domain="[('customer','=',True)]")
    num_sinister = fields.Char(string="Number of sinister")
    number_current_file = fields.Integer(
        'Number of current file',
        compute='_get_data', store=True)
    last_complete_instance = fields.Char(
        'Last complete Instance',
        compute='_get_data', store=True)
    part_ids = fields.One2many('legal.part', 'prosecution_id', string='Parts')
    note = fields.Text('Notes')
    negotiation_ids = fields.One2many(
        'legal.negotiation', 'prosecution_id', string="Negotiation")
    evidence_ids = fields.One2many(
        'legal.evidence', 'prosecution_id', string="Evidence")
    audiences_ids = fields.One2many(
        'legal.audiences', 'prosecution_id', string="Audiences")
    expertise_ids = fields.One2many(
        'legal.expertise', 'prosecution_id', string="Expertise")
    description_of_claim = fields.Text(string='Description of claim')

    @api.one
    def set_open(self):
        self.general_state = 'open'
        self.re_opening_date_folder = date.today()

    @api.one
    def set_close(self):
        self.general_state = 'closed'
        self.close_date_folder = date.today()
        self.re_opening_date_folder = False


class legal_type_prosecution(models.Model):

    """"""

    _name = 'legal.prosecution_type'
    _description = 'type prosecution'

    name = fields.Char('Name')
    code = fields.Integer('Code')
