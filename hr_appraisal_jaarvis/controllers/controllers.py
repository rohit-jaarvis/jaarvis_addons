# -*- coding: utf-8 -*-
from odoo import http

# class HrAppraisalJaarvis(http.Controller):
#     @http.route('/hr_appraisal_jaarvis/hr_appraisal_jaarvis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_appraisal_jaarvis/hr_appraisal_jaarvis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_appraisal_jaarvis.listing', {
#             'root': '/hr_appraisal_jaarvis/hr_appraisal_jaarvis',
#             'objects': http.request.env['hr_appraisal_jaarvis.hr_appraisal_jaarvis'].search([]),
#         })

#     @http.route('/hr_appraisal_jaarvis/hr_appraisal_jaarvis/objects/<model("hr_appraisal_jaarvis.hr_appraisal_jaarvis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_appraisal_jaarvis.object', {
#             'object': obj
#         })