# -*- coding: utf-8 -*-
from odoo import http

# class HrExitJaarvis(http.Controller):
#     @http.route('/hr_exit_jaarvis/hr_exit_jaarvis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_exit_jaarvis/hr_exit_jaarvis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_exit_jaarvis.listing', {
#             'root': '/hr_exit_jaarvis/hr_exit_jaarvis',
#             'objects': http.request.env['hr_exit_jaarvis.hr_exit_jaarvis'].search([]),
#         })

#     @http.route('/hr_exit_jaarvis/hr_exit_jaarvis/objects/<model("hr_exit_jaarvis.hr_exit_jaarvis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_exit_jaarvis.object', {
#             'object': obj
#         })