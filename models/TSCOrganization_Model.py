# Organization in TSC

from odoo import models, fields, api

class TSCOrganization(models.Model):
    _name = 'tsc.organization'
    _description = 'Organization in TSC'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    OrganizationCategory = [
        ('Scientific','Scientific'),
        ('Academic','Academic'),
        ('Ministry of Defence','Ministry of Defence')
    ]
    name = fields.Char(string='Organization Code', required=True, tracking=True)
    eng_name = fields.Char(string='Organization Name (English)', required=True, tracking=True)
    thai_name = fields.Char(string='Organization Name (Thai)', required=True, tracking=True)
    image_org = fields.Image(string='Picture of organization',
                             max_width=200, max_height=200, required=True, tracking=True)
    organization_category = fields.Selection(OrganizationCategory, string='Organization Category', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Organization name already exists !"),
    ]