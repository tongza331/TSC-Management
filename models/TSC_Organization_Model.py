# Organization in TSC

from odoo import models, fields, api

class TSCOrganization(models.Model):
    _name = 'tsc.organization'
    _description = 'Organization in TSC'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id'

    OrganizationCategory = [
        ('Scientific', 'Scientific'),
        ('Academic', 'Academic'),
        ('Ministry of Defence', 'Ministry of Defence')
    ]
    name = fields.Char(string='Organization code', required=True, tracking=True)
    eng_name = fields.Char(string='Organization name (English)', required=True, tracking=True)
    thai_name = fields.Char(string='Organization name (Thai)', required=True, tracking=True)
    image_org = fields.Image(string='Photo of organization',
                             max_width=200, max_height=200, required=True, tracking=True)
    organization_category = fields.Selection(OrganizationCategory, string='Organization category', required=True)
    org_link = fields.Char(string='Organization url', tracking=True)

    # Duplicate prevention of name
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Organization name already exists !"),
    ]