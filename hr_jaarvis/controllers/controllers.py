# -*- coding: utf-8 -*-
from odoo import http

# class HrJaarvis(http.Controller):
#     @http.route('/hr_jaarvis/hr_jaarvis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_jaarvis/hr_jaarvis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_jaarvis.listing', {
#             'root': '/hr_jaarvis/hr_jaarvis',
#             'objects': http.request.env['hr_jaarvis.hr_jaarvis'].search([]),
#         })

#     @http.route('/hr_jaarvis/hr_jaarvis/objects/<model("hr_jaarvis.hr_jaarvis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_jaarvis.object', {
#             'object': obj
#         })