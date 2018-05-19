from odoo import models, fields, api


class HrAttandance(models.Model):
    _inherit = 'hr.attendance'

    shift = fields.Char(string='shift')
    status = fields.Char(string='status')
    w_duration = fields.Integer(string='W. duration')
    break_duration = fields.Integer(string='Break Duration')

