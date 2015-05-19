# -*- coding: utf-8 -*-

from openerp import models, fields


class procese(models.Model):

    """"""

    _name = 'legal.procese'
    _description = 'procese'

    caratula = fields.Text(string='Caratula', required=True)
    color = fields.Integer('Color Index')
    type_procese_id = fields.Many2one(
        'legal.procese_type',
        string='Type of process')
    observation = fields.Char(string='Observation')
    folder_name = fields.Char(string='Folder Name')
    responsible_id = fields.Many2one(
        'res.users', string='Responsible', domain="[('is_lawyer','=',True)]")
    access_level = fields.Selection(
        [('level_1', 'Level 1'),
         ('level_2', 'Level 2'), ('level_3', 'Level 3'),
         ('level_4', 'Level 4'), ('level_5', 'Level 5'),
         ('supervisor', 'Supervisor'), ('reserved', 'Reserved')],
        'Access Level')
    status_id = fields.Many2one('legal.status', string='Status')
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    radicacion_ids = fields.One2many(
        'legal.radication', 'procese_id', string='Radicacion')
    claims_ids = fields.One2many('legal.claims', 'procese_id', string='Claims')
    auxiliary_fields_ids = fields.One2many(
        'legal.auxiliary', 'procese_id', string='Auxiliary Fields')
    other_types_of_processes_ids = fields.One2many(
        'legal.other_types_of_processes',
        'procese_id', string='Other types of processes')


class legal_type_procese(models.Model):

    """"""

    _name = 'legal.procese_type'
    _description = 'type procese'

    name = fields.Char('Name')


class legal_other_types_of_processes(models.Model):

    """"""

    _name = 'legal.other_types_of_processes'

    name = fields.Char('Description')
    procese_id = fields.Many2one('legal.procese', string='Procese')
