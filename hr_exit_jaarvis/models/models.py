# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class hr_exit(models.Model):
    _name = 'hr_exit_jaarvis.hr_exit'
    _description = 'Hr Exit'
    _order = 'request_date desc, name'

    def _default_employee(self):
        return self.env.context.get('default_employee_id') or self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1)

    name = fields.Char(string = 'Name')
    employee_id = fields.Many2one('hr.employee',string = 'Employee',default=_default_employee)
    partner_id = fields.Many2one('res.partner','employee_id.partner_id')
    # work_location = fields.Related('employee_id.work_location', string='Work Location')
    # job_id = fields.Related('employee_id.job_id', string='Designation')
    # date_of_joinin

    request_date = fields.Datetime(string = 'Request Date',default=lambda self: datetime.now())

    # IT clearence
    # should be done only by It person
    is_delete_email_id = fields.Boolean(string='Delete Email Id')
    is_laptop_returned = fields.Boolean(string='Laptop Returned')
    is_system_login_ids_deactivated = fields.Boolean(string='System Login Ids Deactivated')
    is_skypr_id_deactivated = fields.Boolean(string='Skype Id Deactivated')
    any_other_review_and_it_assets = fields.Text(string='Any other Remarks or IT Assets')
    it_clearence_remarks = fields.Text(string='Remarks')

    # Administration Clearance
    is_desk_cabin_key_returned = fields.Boolean(string='Desk or Cabin key Returned')
    is_id_card_handover = fields.Boolean(string='Id car handover')
    is_card_returned_company = fields.Boolean(string='Card Retuned Company')
    is_owned_sim_card_liabrary = fields.Boolean(string='Own Sim Card Liabrary')
    is_book_handover = fields.Boolean(string='Book HandOver')
    admin_clearence_remarks = fields.Text(string='Remarks')

    #Finance Clearance
    is_salary_advance_recovery = fields.Boolean(string='Salary Advance Recovery')
    is_any_imprest_amount_pending = fields.Boolean(string='Any Imprest Amount Pending')
    is_incentive_variable_to_be_paid = fields.Boolean(string='Incentive Variable To be Paid')
    is_all_financial_authority_revoked = fields.Boolean(string='All Financial Authority Revoked')
    is_traning_cost_recovered = fields.Boolean(string='Traning Cost To Be Recovered')
    finance_clearence_remarks = fields.Text(string='Remarks')

    # Reporting Manager Clearence
    is_handover_given_and_report_submitted = fields.Boolean(string='HandOver Given And Report Submitted')
    is_woking_responsibilities_compleated = fields.Boolean(string='Working Responsibilities Compleated')
    is_email_id_retained = fields.Boolean(string='Email Id(To Be Retained/Deleted)')
    is_company_document_manuals_returned = fields.Boolean(string='Company Documents Manual Returned')
    reporting_manager_clearence_remarks = fields.Text(string='Remarks')

    #Hr Clrarence
    is_notice_period_shortfall = fields.Boolean(string='Notice Period Shortfall',groups='hr.group_hr_manager')
    is_exit_interview_conducted = fields.Boolean(string='Exit Interview conducted',groups='hr.group_hr_manager')
    is_ohrm_login_disabled = fields.Boolean(string='OHRM Login Disabled',groups='hr.group_hr_manager')
    is_insaurence_cancelation = fields.Boolean(string='Insaurance Cancelation',groups='hr.group_hr_manager')
    is_any_other = fields.Text(string='Any Other',groups='hr.group_hr_manager')
    hr_clearance_remark = fields.Text(string='Remark',groups='hr.group_hr_manager')


    @api.multi
    def _get_printed_report_name(self):
        return 'Employee_Exit_Form_Name{}_ID{}'.format(self.employee_id.name,self.employee_id.id)

