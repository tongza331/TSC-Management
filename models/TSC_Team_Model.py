# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models
from odoo import tools, _
from odoo.modules.module import get_module_resource


class TSCTeam(models.Model):
    _name = 'tsc.team'
    _description = 'Team profile in TSC'
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
    organization_id = fields.Many2one('tsc.organization', string='Organization', tracking=True, ondelete='set null')
    email = fields.Char(string='Email')
    date_join = fields.Date(string='Date joined')

    @api.model
    def _default_image(self):
        image_path = get_module_resource('tsc', 'static/src/img', 'avatar.png')
        return base64.b64encode(open(image_path, 'rb').read())

    image_team = fields.Image("Your photo", default=_default_image, attachment=True, max_width=300, max_height=300)

