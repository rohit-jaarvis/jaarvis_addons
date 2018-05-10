from odoo import api, fields, models
import datetime
from dateutil.relativedelta import relativedelta
import pymysql
import pymysql.cursors

config ={
    'host' : '192.168.245.35',
    'port' : 33306,
    'user' : 'jaarvis',
    'password' : 'jaarvis',
    'db' : 'epushserver',
    'charset': 'utf8mb4' ,
    'cursorclass' : pymysql.cursors.DictCursor

}

class LastImportEmployeeDetail(models.Model):
    """here we will download the employee data from essl epushserver
    and put into the hr.employee"""
    _name = 'hr.employee.last.import.essl.detail'

    last_time_of_import = fields.Datetime(
                                            'Last Import Date',
                                            default=datetime.datetime.now() - relativedelta(months=2)
                                            )



class WizardImportEmployeeData(models.TransientModel):
    _name = 'wizard.import.employee.data'

    @api.multi
    def import_employee_data(self):
        query = "select EmployeeName as name ,EmployeeCodeInDevice as biometric_id from employees;"
        emp_data = self.fetch_data_from_epush_server(query,config)
        emp = self.env['hr.employee']
        [emp.create(data) for data in emp_data]


    @staticmethod
    def fetch_data_from_epush_server(query,config):
        """this function will connect to the remote my sql database details provided in config dict"""
        conn = pymysql.connect(**config)
        cr = conn.cursor()
        cr.execute(query)
        data = cr.fetchall()
        return data


fetch_data = WizardImportEmployeeData.fetch_data_from_epush_server



