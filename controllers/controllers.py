# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request

class WebsiteTSC(http.Controller):
    @http.route('/team', auth='public', website=True)
    def team_list(self, **kw):
        leader_team = http.request.env['tsc.team'].search([('position', '=', 'Leader')])
        advisor_team = http.request.env['tsc.team'].search([('position', '=', 'Advisor')])
        researcher_team = http.request.env['tsc.team'].search([('position', '=', 'Researcher')])
        engineer_team = http.request.env['tsc.team'].search([('position', '=', 'Engineer')])
        return http.request.render("tsc.team_list",{
            'leader_team': leader_team,
            'advisor_team': advisor_team,
            'researcher_team': researcher_team,
            'engineer_team': engineer_team,
        })

    @http.route(['/team/details/<model("tsc.team"):member>'],
                type='http', auth='public', website=True)
    def team_detail(self, member):
        values = {'member': member}
        return http.request.render("tsc.team_detail", values)

    @http.route(['/career/job', '/career/job/page/<int:page>'],
                type='http', auth='public', website=True)
    def job_list(self, page=0):
        domain = [('career_category', '=', 'Job')]
        total_jobs = http.request.env['tsc.career'].search(domain)
        total_count = len(total_jobs)
        per_page = 5

        # total : Total count of records
        # Page : Current page
        # Step : Count of records need to display in one page
        # Scope : Count of pages needs to display in paper at a time

        pager = request.website.pager(url='/career/job', total=total_count, page=page, step=per_page, scope=3, url_args=None)

        # offset = Count to exclude (first n)
        jobs = request.env['tsc.career'].search(domain, limit=per_page, offset=pager['offset'], order='create_date desc')
        return http.request.render("tsc.job_list",{
            'jobs': jobs,
            'pager': pager,
        })

    @http.route(['/career/intern', '/career/intern/page/<int:page>'],
                type='http', auth='public', website=True)
    def intern_list(self, page=0):
        domain = [('career_category', '=', 'Internship')]
        # domain = []
        total_interns = http.request.env['tsc.career'].search(domain)
        total_count = len(total_interns)
        per_page = 10

        # total : Total count of records
        # Page : Current page
        # Step : Count of records need to display in one page
        # Scope : Count of pages needs to display in paper at a time

        pager = request.website.pager(url='/career/intern', total=total_count, page=page, step=per_page, scope=3, url_args=None)

        # offset = Count to exclude (first n)
        intern = request.env['tsc.career'].search(domain, limit=per_page, offset=pager['offset'], order='create_date desc')
        return http.request.render("tsc.intern_list", {
            'intern': intern,
            'pager': pager,
        })