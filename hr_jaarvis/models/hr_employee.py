# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Hr Employee Jaarvis'

    current_address = fields.Char(string='Current Address')
    permanent_address = fields.Char(string='Permanent Address')
    father_name = fields.Char(string="Father's Name")
    emergency_contact_name = fields.Char(string='Emergency Contact Name')
    universal_account_number = fields.Char(string='UAN(Universal Account Number)')
    pan_id = fields.Char(string = 'Pan No')
    aadhar_id = fields.Char(string = 'Aadhar No')
