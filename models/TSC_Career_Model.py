
from odoo import models, fields, api

class TSCCareer(models.Model):
    _name = 'tsc.career'
    _description = 'Career in TSC'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "create_date desc, day_left asc"

    CareerTag = [
        ('Announcement', 'Announcement'),
        ('Hiring', 'Hiring')
    ]

    CareerCategory = [
        ('Job', 'Job'),
        ('Internship', 'Internship')
    ]
    name = fields.Char(string='Career title', required=True, tracking=True)
    career_detail = fields.Text(string='Career detail', required=True, tracking=True)
    work_at = fields.Many2one('tsc.organization', 'Work at', ondelete='set null')
    career_link = fields.Char(string='Career url', required=True, tracking=True)
    career_category = fields.Selection(CareerCategory, string='Career category', required=True)
    career_tag = fields.Selection(CareerTag, string='Career tag', required=True)
    open_date = fields.Date(string='Start date',default=fields.Date.today(), required=True)
    expired_date = fields.Date(string='End date')
    day_left = fields.Char(string='Day left', readonly=True, compute='_compute_difference')
    create_date = fields.Date('Created on', default=fields.Date.today(), index=True, readonly=True)

    @api.depends('expired_date', 'create_date', 'day_left')
    def _compute_difference(self):
        for rec in self:
            if rec.open_date and rec.expired_date:
                if rec.create_date > rec.expired_date:
                    rec.day_left = '0'
                else:
                    end_date = rec.expired_date
                    today_date = rec.create_date
                    rec.day_left = (end_date-today_date)
                    temp_str = str(int(rec.day_left[:2])+1)
                    rec.day_left = temp_str.replace(rec.day_left[:2],temp_str)
            elif (rec.expired_date is False) or (rec.open_date is False):
                rec.day_left = 'No information'


