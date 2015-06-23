# -*- coding: utf-8 -*-

from openerp import models, fields, api


class process(models.Model):

    """"""

    _name = 'legal.process'
    _description = 'process'
    _inherit = ['mail.thread']
    _rec_name = 'folder_name'

    @api.one
    def action_compute(self):
        name = ''
        if self.partner_id:
            name = self.partner_id.name[0]
        if self.process_type_id:
            name += '-' + str(self.process_type_id.code)
        name += '-' + self.env['ir.sequence'].get('legal.process')
        self.folder_name = name

    def create(self, cr, uid, vals, context=None):
        name = ''
        partner_obj = self.pool['res.partner']
        process_type_obj = self.pool['legal.process_type']
        if vals.get('partner_id', False):
            name = partner_obj.browse(
                cr, uid, vals.get('partner_id', False), context=context).name[0]
        if vals.get('process_type_id', False):
            name += '-' + str(process_type_obj.browse(cr, uid,
                                                      vals.get('process_type_id', False), context=context).code)
        name += '-' + self.pool['ir.sequence'].get(cr, uid, 'legal.process')
        vals['folder_name'] = name
        return super(process, self).create(cr, uid, vals, context=None)

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

    caratula = fields.Char(string='Caratula', required=True)
    color = fields.Integer('Color Index')
    sequence = fields.Char('Sequence')
    process_type_id = fields.Many2one(
        'legal.process_type',
        string='Type of process')
    folder_name = fields.Char(
        string='Folder Name', readonly=True)
    responsible_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer', domain="[('is_lawyer','=',True)]")
    responsibility_id = fields.Many2one(
        'legal.responsibility', string='Responsibility')
    general_state = fields.Selection(
        [('open', 'Open'),
         ('closed', 'Closed')],
        'General State', default='open')
    status_id = fields.Many2one('legal.status', string='Status')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    radication_ids = fields.One2many(
        'legal.radication', 'process_id', string='Radication')
    claim_ids = fields.One2many('legal.claim', 'process_id', string='Claims')
    claim_type_ids = fields.Many2many(
        'legal.claim.type',
        'legal_type_claim_ids_process_id_rel',
        'process_id',
        'name', string='Type of Claims')
    auxiliary_ids = fields.One2many(
        'legal.auxiliary', 'process_id', string='Auxiliary Fields')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_process_ids_rel',
        'process_id',
        'attachment_id', string='Attachments')
    regulation_ids = fields.One2many(
        'legal.regulation', 'process_id', string='Regulation')
    substate_id = fields.Many2one('legal.substate', string="Substate")
    current_judged_id = fields.Many2one(
        'legal.office',
        string='Current Judged', compute='_get_data', store=True)
    event_ids = fields.One2many(
        'legal.event', 'process_id', string="Events")
    partner_id = fields.Many2one(
        'res.partner', 'Customer', domain="[('customer','=',True)]")
    num_sinister = fields.Char(string="Number of sinister")
    number_current_file = fields.Integer(
        'Number of current file',
        compute='_get_data', store=True)
    last_complete_instance = fields.Char(
        'Last complete Instance',
        compute='_get_data', store=True)
    part_ids = fields.One2many('legal.part', 'process_id', string='Parts')
    note = fields.Text('Notes')
    negotiation_ids = fields.One2many(
        'legal.negotiation', 'process_id', string="Negotiation")
    evidence_ids = fields.One2many(
        'legal.evidence', 'process_id', string="Evidence")

    @api.one
    def set_open(self):
        self.general_state = 'open'

    @api.one
    def set_close(self):
        self.general_state = 'closed'


class legal_type_process(models.Model):

    """"""

    _name = 'legal.process_type'
    _description = 'type process'

    name = fields.Char('Name')
    code = fields.Integer('Code')
