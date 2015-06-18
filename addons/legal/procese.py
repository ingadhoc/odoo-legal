# -*- coding: utf-8 -*-

from openerp import models, fields, api


class procese(models.Model):

    """"""

    _name = 'legal.procese'
    _description = 'procese'
    _inherit = ['mail.thread']

    @api.one
    def _get_total_claim(self):
        total = 0.0
        for claim in self.claims_ids:
            total += claim.total_claim
        self.amount_total_claim = total

    @api.one
    def _get_total_regulation(self):
        total = 0.0
        for regulation in self.regulation_ids:
            total += regulation.amount_regulation
        self.amount_total_regulation = total

    def create(self, cr, uid, vals, context=None):
        name = ''
        partner_obj = self.pool['res.partner']
        procese_type_obj = self.pool['legal.procese_type']
        if vals.get('partner_id', False):
            name = partner_obj.browse(
                cr, uid, vals.get('partner_id', False), context=context).name[0]
        if vals.get('type_procese_id', False):
            name += '-' + str(procese_type_obj.browse(cr, uid,
                                                      vals.get('type_procese_id', False), context=context).code)
        name += self.pool['ir.sequence'].get(cr, uid, 'legal.procese')
        vals['folder_name'] = name
        return super(procese, self).create(cr, uid, vals, context=None)

    @api.one
    @api.depends('radication_ids')
    def _get_data(self):
        if self.radication_ids:
            self.current_judged_id = self.radication_ids[
                0].current_judged_id.id
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
    type_procese_id = fields.Many2one(
        'legal.procese_type',
        string='Type of process')
    folder_name = fields.Char(
        string='Folder Name', readonly=True)
    responsible_id = fields.Many2one(
        'res.users',
        string='Responsible Lawyer', domain="[('is_lawyer','=',True)]")
    general_state = fields.Selection(
        [('open', 'Open'),
         ('closed', 'Closed')],
        'General State', default='open')
    status_id = fields.Many2one('legal.status', string='Status')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    radication_ids = fields.One2many(
        'legal.radication', 'procese_id', string='Radicacion')
    claims_ids = fields.One2many('legal.claims', 'procese_id', string='Claims')
    type_claims_ids = fields.Many2many(
        'legal.claims_type',
        'legal_type_claims_ids_procese_id_rel',
        'procese_id',
        'name', string='Type of Claims')
    auxiliary_fields_ids = fields.One2many(
        'legal.auxiliary', 'procese_id', string='Auxiliary Fields')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'legal_attachment_ids_procese_ids_rel',
        'procese_id',
        'attachment_id', string='Attachments')
    regulation_ids = fields.One2many(
        'legal.regulation', 'procese_id', string='Regulation')
    substate_id = fields.Many2one('legal.substate', string="Substate")
    current_judged_id = fields.Many2one(
        'legal.office',
        string='Current Judged', compute='_get_data', store=True)
    events_ids = fields.One2many(
        'legal.events', 'procese_id', string="Events")
    partner_id = fields.Many2one(
        'res.partner', 'Partner', domain="[('customer','=',True)]")
    num_sinister = fields.Char(string="Number of sinister")
    number_current_file = fields.Integer(
        'Number of current file',
        compute='_get_data', store=True)
    last_complete_instance = fields.Char(
        'Last complete Instance',
        compute='_get_data', store=True)
    part_ids = fields.One2many('legal.parts', 'procese_id', string='Parts')
    amount_total_claim = fields.Float(
        string='Total', compute='_get_total_claim')
    amount_total_regulation = fields.Float(
        string='Total', compute='_get_total_regulation')
    note = fields.Text('Notes')
    negotiation_ids = fields.One2many(
        'legal.negotiation', 'procese_id', string="Negotiation")
    test_ids = fields.One2many(
        'legal.tests', 'procese_id', string="Tests")

    @api.one
    def set_open(self):
        self.general_state = 'open'

    @api.one
    def set_close(self):
        self.general_state = 'closed'


class legal_type_procese(models.Model):

    """"""

    _name = 'legal.procese_type'
    _description = 'type procese'

    name = fields.Char('Name')
    code = fields.Integer('Code')
