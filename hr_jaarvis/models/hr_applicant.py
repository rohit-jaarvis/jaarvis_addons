from odoo import models, fields, api


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    date = fields.Datetime(string='Date')
    date_of_interview = fields.Datetime(string='Interview Date')
    mode_of_interview = fields.Char(string='Mode of Interview')
    experience = fields.Integer(string='Experience in years')
    notice_period = fields.Integer(string='Notice Period(in months)')