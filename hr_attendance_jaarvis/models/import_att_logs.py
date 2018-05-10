from datetime import datetime,timedelta,date,time

from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from dateutil.relativedelta import relativedelta

from .import_emp import config,fetch_data
import pytz



last_device_log_id = 0
ind_timezone = pytz.timezone("Asia/Kolkata")
utc_timezone = pytz.timezone("UTC")




class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.model
    def put_data_in_odoo_db(self, data):

        emp_model = self.env['hr.employee']
        att_model = self
        for biomatric_id, value in data.items():
            emp_obj = emp_model.search([('biometric_id', '=', biomatric_id)])
            if len(emp_obj) >= 1:
                att_values = dict(employee_id=emp_obj[0].id,
                                  check_in=value[0],
                                  check_out=value[1]
                                  )
                att_model.create(att_values)

        pass

    @api.model
    def import_att_logs_from_biometric(self):
        today_date = date.today()
        today_end_time = datetime.combine(date.today(), time(23,59,59))
        today_start_time = datetime.combine(date.today(), time())
        table_name = "devicelogs_%s_%s"%(today_date.month,today_date.year)
        query = "SELECT UserId ,LogDate,Direction FROM \
                  %s WHERE DATE(`LogDate`) = CURDATE();"%(table_name)

        att_data = fetch_data(query,config)

        refined_data = {}
        for data in att_data:
            if refined_data.get(data['UserId'],False):
                refined_data[data['UserId']][0] = min(refined_data[data['UserId']][0], data['LogDate'])
                refined_data[data['UserId']][1] = max(refined_data[data['UserId']][1], data['LogDate'])
            else:
                refined_data[data['UserId']] = [today_end_time,today_start_time]
                refined_data[data['UserId']][0] = min(refined_data[data['UserId']][0], data['LogDate'])
                refined_data[data['UserId']][1] = max(refined_data[data['UserId']][1], data['LogDate'])

        refined_data.update({k: self.convert_ind_to_utc(*v) for k, v in refined_data.items()})
        self.put_data_in_odoo_db(refined_data)


    @staticmethod
    def convert_ind_to_utc(ind_date_time1,ind_date_time2):
        utc_date_time1 = ind_timezone.localize(ind_date_time1).astimezone(utc_timezone)
        utc_date_time2 = ind_timezone.localize(ind_date_time2).astimezone(utc_timezone)
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        return  [utc_date_time1.strftime(fmt),utc_date_time2.strftime(fmt)]





