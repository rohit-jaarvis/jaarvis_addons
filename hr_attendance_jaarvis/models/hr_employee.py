# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    biometric_id = fields.Char(string='Biometric Employee Code')

    _sql_constraints = [('biometric_id_uniq', 'unique (biometric_id)',"for uniqueness of boi id")]



