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
    nominee_pf = fields.Char(string= 'Nominee For Pf')
    internship_confirmation_date = fields.Date('Internship Confirmation Date')
    probation_completion_date = fields.Date('Probation Completion Date')

    ####Details of last organization
    previous_company_name = fields.Char('Company name')
    previous_company_hr_name = fields.Char('Hr name')
    previous_company_hr_contact = fields.Char('Hr Contact No')

    #total_experience
    experience_total_years = fields.Integer(string='Years')
    experience_months = fields.Integer(string='Months')

