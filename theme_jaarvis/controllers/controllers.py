# -*- coding: utf-8 -*-
from odoo import http

# class /odoo/custom/addons/themeJaarvis(http.Controller):
#     @http.route('//odoo/custom/addons/theme_jaarvis//odoo/custom/addons/theme_jaarvis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/addons/theme_jaarvis//odoo/custom/addons/theme_jaarvis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/addons/theme_jaarvis.listing', {
#             'root': '//odoo/custom/addons/theme_jaarvis//odoo/custom/addons/theme_jaarvis',
#             'objects': http.request.env['/odoo/custom/addons/theme_jaarvis./odoo/custom/addons/theme_jaarvis'].search([]),
#         })

#     @http.route('//odoo/custom/addons/theme_jaarvis//odoo/custom/addons/theme_jaarvis/objects/<model("/odoo/custom/addons/theme_jaarvis./odoo/custom/addons/theme_jaarvis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/addons/theme_jaarvis.object', {
#             'object': obj
#         })