# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TSCTeam(models.Model):
    _name = 'tsc.team'
    _description = 'Team in TSC'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    position_choice = [
        ('Leader', 'Leadership'),
        ('Advisor', 'Advisor'),
        ('Researcher', 'Researcher'),
        ('Engineer', 'Engineer')
    ]

    name = fields.Char(string='Firstname Lastname', required=True, tracking=True, translate=True)
    position = fields.Selection(position_choice, string='Position in TSC', required=True, tracking=True)
    position_detail = fields.Char(string='Position detail', required=True, tracking=True)
    organization_id = fields.Many2one('tsc.organization',string='Organization', tracking=True, ondelete='set null')
    email = fields.Char(string='Email')
    date_join = fields.Date(string='Date joined')
    image_team = fields.Image(string='Your image',
                       max_width=500, max_height=500, required=True)
